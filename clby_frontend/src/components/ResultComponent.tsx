import {ResultManovaDTO} from "../DTOs/ResultManovaDTO.tsx";
import ResultManovaComponent from "./ResultManovaComponent.tsx";
import ResultAverageComponent from "./ResultAverageComponent.tsx";
import ResultClusterComponent from "./ResultClusterComponent.tsx";

export default function ResultComponent(props: { result: ResultManovaDTO, type: string }) {

    return (
        <div>
            {
                props.type === "manova" ? (
                    <ResultManovaComponent result={props.result}/>
                ) : null
            }
            {
                props.type === "average" ? (
                    <ResultAverageComponent result={props.result}/>
                ) : null
            }
            {
                props.type === "cluster" ? (
                    <ResultClusterComponent result={props.result}/>
                ) : null
            }
        </div>
    );
}