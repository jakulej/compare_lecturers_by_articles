import 'bootstrap/dist/css/bootstrap.css';
// import {useState} from "react";
// import {LecturerDTO} from "../../DTOs/LecturerDTO.tsx";
// import {ManovaResultDTO} from "../../DTOs/ManovaResultDTO.tsx";
// import {ComparisonDTO} from "../../DTOs/ComparisonDTO.tsx";
// import {ComparisonComponent} from "./ComparisonComponent";

import jsonData from '../../assets/data.json';
// import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import LecturerComponent from "../Lecturer/LecturerComponent.tsx";
import ResultComponent from "../Result/ResultComponent.tsx";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function ComparisonList() {
    // const [lecturers, setLecturers] = useState<LecturerDTO[] | null>();
    // const [results, setResults] = useState<ManovaResultDTO | null>();
    // const [comparisons, setComparisons] = useState<ComparisonDTO | null>();
    //
    // useEffect(() => {
    //     axios
    //         .get(baseURL + '...')
    //         .then((response) => {
    //             setLecturers(response.data);
    //             console.log(response);
    //         })
    //         .catch(error => console.log(error));
    // }, []);
    //
    // useEffect(() => {
    //     axios
    //         .get(baseURL + '...')
    //         .then((response) => {
    //             setResults(response.data);
    //             console.log(response);
    //         })
    //         .catch(error => console.log(error));
    // }, []);
    //
    // const submitHandler = (event) => {
    //     event.preventDefault();
    //
    //
    // };
    //
    // return (
    //     <div>
    //         <div className="row row-cols-1 row-cols-md-2 g-4">
    //             {comparisons
    //                 ? comparisons.map((comparison, i) => (
    //                     <div key={i}>
    //                         <ComparisonComponent lecturers={lecturers} resu/>
    //                     </div>
    //             ))};
    //         </div>
    //
    //
    //
    //         <button className="btn btn-success mb-3">
    //             <i className="fa-solid fa-plus"></i>
    //             <a> Add comparison</a>
    //         </button>
    //     </div>
    // );

    const options = {
        responsive: true,
        plugins: {
            legend: {
                display: false,
            },
            title: {
                display: true,
                text: 'Bar Graph Representation',
            },
        },
    };

    return (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '2rem' }}>
            {Object.entries(jsonData).map(([key, values]) => {
                const labels = Object.keys(values);
                const colors = labels.map((_, index) => `hsl(${(index * 360) / labels.length}, 70%, 50%)`);
                const data = {
                    labels,
                    datasets: [
                        {
                            label: key,
                            data: Object.values(values),
                            backgroundColor: colors,
                            borderColor: colors,
                            borderWidth: 1,
                        },
                    ],
                };

                return (
                    <div key={key} style={{flex: '1 1 calc(50% - 2rem)', marginBottom: '2rem'}}>
                        <div className="input-group mb-3">
                            <select className="form-select" aria-label="Default select example">
                                <option selected>Wybierz metodę</option>
                                <option value="1">Metoda Manowa</option>
                                <option value="2">Metoda Średniej</option>
                                <option value="3">Analiza skupień</option>
                            </select>
                            <button className="btn btn-outline-secondary" type="button" id="button-addon2">Porównaj
                            </button>
                        </div>
                        <div style={{ display: 'flex', gap: '1rem' }}>
                            <LecturerComponent/>
                            <LecturerComponent/>
                        </div>
                        <ResultComponent/>
                        <h3>{key}</h3>
                        <Bar data={data} options={options}/>
                    </div>
                );
            })}
        </div>
    );
}