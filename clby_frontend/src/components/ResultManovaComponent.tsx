import {ResultManovaDTO} from "../DTOs/ResultManovaDTO.tsx";

export default function ResultComponent(props: { result: ResultManovaDTO}) {
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
                        <td>{(Math.round((props.result.Value["Wilks' lambda"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["F Value"]["Wilks' lambda"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["Pr > F"]["Wilks' lambda"])*1000))/1000}</td>
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
                        <td>{(Math.round((props.result.Value["Pillai's trace"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["F Value"]["Pillai's trace"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["Pr > F"]["Pillai's trace"])*1000))/1000}</td>
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
                        <td>{(Math.round((props.result.Value["Hotelling-Lawley trace"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["F Value"]["Hotelling-Lawley trace"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["Pr > F"]["Hotelling-Lawley trace"])*1000))/1000}</td>
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
                        <td>{(Math.round((props.result.Value["Roy's greatest root"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["F Value"]["Roy's greatest root"])*1000))/1000}</td>
                        <td>{(Math.round((props.result["Pr > F"]["Roy's greatest root"])*1000))/1000}</td>
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
