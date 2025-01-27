import {ResultDTO} from "../DTOs/ResultDTO.tsx";
import ResultManovaComponent from "./ResultManovaComponent.tsx";
import ResultAverageComponent from "./ResultAverageComponent.tsx";
import ResultClusteringComponent from "./ResultClusteringComponent.tsx";

export default function ResultComponent(props: { result: ResultDTO, type: string }) {

    return (
        <div>
            {
                props.type === "manova_method" ? (
                    <ResultManovaComponent result={props.result}/>
                ) : null
            }
            {
                props.type === "average_method" ? (
                    <ResultAverageComponent result={props.result}/>
                ) : null
            }
            {
                props.type === "data_clustering" ? (
                    <ResultClusteringComponent result={props.result}/>
                ) : null
            }
        </div>
    );
}