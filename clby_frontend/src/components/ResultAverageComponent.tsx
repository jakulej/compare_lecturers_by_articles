import {ResultDTO} from "../DTOs/ResultDTO.tsx";

export default function ResultAverageComponent(props: { result: ResultDTO}) {
    type Average = {
        wilksLambda: {
            val: number;
            pVal: number;
            conclusions: string;
        };
        pillaisTrace: {
            val: number;
            pVal: number;
            conclusions: string;
        };
        hotellingLawleyTrace: {
            val: number;
            pVal: number;
            conclusions: string;
        };
        roysGreatestRoot: {
            val: number;
            pVal: number;
            conclusions: string;
        };
    };

    function isAverage(data: unknown): data is Average {
        return (
            typeof data === "object" &&
            data !== null &&
            "wilksLambda" in data &&
            "pillaisTrace" in data &&
            "hotellingLawleyTrace" in data &&
            "roysGreatestRoot" in data
        );
    }

    if (isAverage(props.result.advanced)) {
        return (
            <div className="container mt-4">
                <table className="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>Miara</th>
                        <th>Wartość</th>
                        <th>P-wartość</th>
                        <th>Wnioski</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Wilk's Lambda</td>
                        <td>{props.result.advanced.wilksLambda.val}</td>
                        <td>{props.result.advanced.wilksLambda.pVal}</td>
                        <td>{props.result.advanced.wilksLambda.conclusions}</td>
                    </tr>
                    <tr>
                        <td>Pillai's Trace</td>
                        <td>{props.result.advanced.pillaisTrace.val}</td>
                        <td>{props.result.advanced.pillaisTrace.pVal}</td>
                        <td>{props.result.advanced.pillaisTrace.conclusions}</td>
                    </tr>
                    <tr>
                        <td>Hotelling-Lawley Trace</td>
                        <td>{props.result.advanced.hotellingLawleyTrace.val}</td>
                        <td>{props.result.advanced.hotellingLawleyTrace.pVal}</td>
                        <td>{props.result.advanced.hotellingLawleyTrace.conclusions}</td>
                    </tr>
                    <tr>
                        <td>Roy's Greatest Root</td>
                        <td>{props.result.advanced.roysGreatestRoot.val}</td>
                        <td>{props.result.advanced.roysGreatestRoot.pVal}</td>
                        <td>{props.result.advanced.roysGreatestRoot.conclusions}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        )
    } else {
        return <div>Invalid data</div>;
    }
}