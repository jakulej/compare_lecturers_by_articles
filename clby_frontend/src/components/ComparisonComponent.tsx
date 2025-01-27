import {useState} from "react";
import {ComparisonDTO} from "../DTOs/ComparisonDTO.tsx";
import {ResultDTO} from "../DTOs/ResultDTO.tsx";
import axios from "axios";
import {API_URL} from "../api/Axios.tsx";
import React from "react";
import ResultComponent from "./ResultComponent.tsx";
import {LecturerDTO} from "../DTOs/LecturerDTO.tsx";

export default function ComparisonComponent (props: { lecturers: LecturerDTO[] }) {
    const [result, setResult] = useState<ResultDTO>();
    const [comparison, setComparison] = useState<ComparisonDTO>();

    const inputHandler = (event: React.ChangeEvent<HTMLInputElement> | React.ChangeEvent<HTMLSelectElement>) => {
        setComparison({
            ...comparison,
            [event.target.name]: event.target.value
        })
    };

    const getResult = () => {
        if (comparison !== undefined) {
            axios
            .post(API_URL + '...', {
                lecturer1: comparison.lecturer1,
                lecturer2: comparison.lecturer2,
                type: comparison.type,
            })
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
                        <option value="manova_method">Metoda Manova</option>
                        <option value="average_method">Metoda Średniej</option>
                        <option value="data_clustering">Analiza skupień</option>
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
                                props.lecturers
                                    ? props.lecturers.map((lecturer, i) => {
                                        return(
                                            <div key={i}>
                                                <option value={lecturer.id}>{lecturer.name} {lecturer.surname}</option>
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
                                props.lecturers
                                    ? props.lecturers.map((lecturer, i) => {
                                        return(
                                            <div key={i}>
                                                <option value={lecturer.id}>{lecturer.name} {lecturer.surname}</option>
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