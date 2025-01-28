import {useState} from "react";
import {ComparisonDTO} from "../DTOs/ComparisonDTO.tsx";
import {ResultManovaDTO} from "../DTOs/ResultManovaDTO.tsx";
import axios from "axios";
import React from "react";
import ResultComponent from "./ResultComponent.tsx";
import {LecturerDTO} from "../DTOs/LecturerDTO.tsx";
import {API_URL} from "../api/API_Data.tsx";

export default function ComparisonComponent (props: { lecturers: LecturerDTO[] }) {
    const lecturers_temp= props.lecturers || [];
    const [result, setResult] = useState<ResultManovaDTO>();
    const [comparison, setComparison] = useState<ComparisonDTO>();

    const inputHandler = (event: React.ChangeEvent<HTMLInputElement> | React.ChangeEvent<HTMLSelectElement>) => {
        setComparison({
            ...comparison,
            [event.target.name]: event.target.value
        })
    };

    const getResult = () => {
        if (comparison !== undefined && comparison.type !== undefined && comparison.lecturer1 !== undefined && comparison.lecturer2 !== undefined) {
            axios
                .get(API_URL + '/' + comparison.type + '/' + comparison.lecturer1 + '/' + comparison.lecturer2)
                .then((response) => {
                    setResult(response.data);
                    console.log(response);
                })
                .catch(error => console.log(error));
        }
    };

    return (
        <div>
            <div className="card mb-3">
                <div className="input-group mb-3">
                    <select onChange={inputHandler} name={"type"} className="form-select" aria-label="Default select example">
                        <option>Wybierz metodę</option>
                        <option value="manova">Metoda Manova</option>
                        <option value="average">Metoda Średniej</option>
                        <option value="cluster">Analiza skupień</option>
                    </select>
                    <button onClick={getResult} className="btn btn-outline-secondary" type="button" id="button-addon2">Porównaj
                    </button>
                </div>
                <nav>
                    <div>
                        <input onChange={inputHandler} name={"lecturer1"} className="form-control" list="datalistOptions" id="exampleDataList"
                               placeholder="Type to search..."/>
                        <datalist id="datalistOptions">
                            {
                                lecturers_temp
                                    ? lecturers_temp.map((lecturer, i) => {
                                        return(
                                            <div key={i}>
                                                <option value={lecturer.id}>{lecturer.name}</option>
                                            </div>
                                        )}
                                    ): null
                            }
                        </datalist>
                    </div>

                    <div>
                        <input onChange={inputHandler} name={"lecturer2"} className="form-control" list="datalistOptions" id="exampleDataList"
                               placeholder="Type to search..."/>
                        <datalist id="datalistOptions">
                            {
                               lecturers_temp
                                    ? lecturers_temp.map((lecturer, i) => {
                                        return(
                                            <div key={i}>
                                                <option value={lecturer.id}>{lecturer.name}</option>
                                            </div>
                                        )}
                                    ): null
                            }
                        </datalist>
                    </div>
                </nav>
                <div>
                    {
                        comparison !== undefined ? (
                                comparison.type !== undefined ? (
                                        result !== undefined ? (
                                                <ResultComponent result={result} type={comparison.type}/>
                                            )
                                            : null
                                    )
                                    : null
                            )
                            : null
                    }
                </div>
            </div>
        </div>
    );
}