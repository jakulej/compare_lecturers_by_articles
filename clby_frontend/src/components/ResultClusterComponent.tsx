import {ResultClusterDTO} from "../DTOs/ResultClusterDTO.tsx";

export default function ResultClusterComponent(props: { result: ResultClusterDTO}) {
    if (props.result !== undefined) {
        return (
            <div className="container mt-4">
                <table className="table table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>Miara</th>
                        <th>Wartość</th>
                        <th>F-Wartość</th>
                        <th>P-wartość</th>
                        <th>Wnioski</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Wilk's Lambda</td>
                        <td>{props.result.Value["Wilks' lambda"]}</td>
                        <td>{props.result["F Value"]["Wilks' lambda"]}</td>
                        <td>{props.result["Pr > F"]["Wilks' lambda"]}</td>
                        {
                            props.result["Pr > F"]["Wilks' lambda"] < 0.05 ?
                                (
                                    <td>
                                        Bez istotności.
                                    </td>
                                )
                                :
                                (
                                    <td>
                                        Istotne różnice.
                                    </td>
                                )
                        }
                    </tr>
                    <tr>
                        <td>Pillai's Trace</td>
                        <td>{props.result.Value["Pillai's trace"]}</td>
                        <td>{props.result["F Value"]["Pillai's trace"]}</td>
                        <td>{props.result["Pr > F"]["Pillai's trace"]}</td>
                        {
                            props.result["Pr > F"]["Pillai's trace"] < 0.05 ?
                                (
                                    <td>
                                        Bez istotności.
                                    </td>
                                )
                                :
                                (
                                    <td>
                                        Istotne różnice.
                                    </td>
                                )
                        }
                    </tr>
                    <tr>
                        <td>Hotelling-Lawley Trace</td>
                        <td>{props.result.Value["Hotelling-Lawley trace"]}</td>
                        <td>{props.result["F Value"]["Hotelling-Lawley trace"]}</td>
                        <td>{props.result["Pr > F"]["Hotelling-Lawley trace"]}</td>
                        {
                            props.result["Pr > F"]["Hotelling-Lawley trace"] < 0.05 ?
                                (
                                    <td>
                                        Bez istotności.
                                    </td>
                                )
                                :
                                (
                                    <td>
                                        Istotne różnice.
                                    </td>
                                )
                        }
                    </tr>
                    <tr>
                        <td>Roy's Greatest Root</td>
                        <td>{props.result.Value["Roy's greatest root"]}</td>
                        <td>{props.result["F Value"]["Roy's greatest root"]}</td>
                        <td>{props.result["Pr > F"]["Roy's greatest root"]}</td>
                        {
                            props.result["Pr > F"]["Roy's greatest root"] < 0.05 ?
                                (
                                    <td>
                                        Bez istotności.
                                    </td>
                                )
                                :
                                (
                                    <td>
                                        Istotne różnice.
                                    </td>
                                )
                        }
                    </tr>
                    </tbody>
                </table>
            </div>
        )
    } else {
        return <div>Invalid data</div>;
    }
};