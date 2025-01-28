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
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Cosine similarity</td>
                        <td>{props.result.euclidean_similarity}</td>
                    </tr>
                    <tr>
                        <td>Euclidean similarity</td>
                        <td>{props.result.manhattan_similarity}</td>
                    </tr>
                    <tr>
                        <td>Manhattan similarity</td>
                        <td>{props.result.cosine_similarity}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        )
    } else {
        return <div>Invalid data</div>;
    }
};