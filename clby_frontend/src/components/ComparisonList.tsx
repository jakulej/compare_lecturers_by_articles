import 'bootstrap/dist/css/bootstrap.css';
import {useEffect, useState} from "react";
import {LecturerDTO} from "../DTOs/LecturerDTO.tsx";
import axios from "axios";
import ComparisonComponent from "./ComparisonComponent.tsx";
import {API_URL} from "../api/API_Data.tsx";

export default function ComparisonList() {
    const [lecturers, setLecturers] = useState<LecturerDTO[]>([]);
    const [count, setCount] = useState(0);

    useEffect(() => {
        axios
            .get<{ [key: number]: string }>(API_URL + '/people')
            .then((response) => {
                const result = Object.keys(response.data).map(key => ({
                    id: parseInt(key),
                    name: response.data[parseInt(key)]
                }));
                setLecturers(result);
                console.log(response);
            })
            .catch(error => console.log(error));
    }, []);

    const addComparison = () => {
        setCount(count + 1);
    };

    return (
        <div>
            <div className="col-12 col-md-4 mb-2">
                {
                    Array.from({ length: count }, (_, i) => (
                        <div key={i}>
                            <ComparisonComponent lecturers={lecturers}/>
                        </div>
                    ))
                }
            </div>
            <div className="col-12 col-md-4 mb-2">
                <div className="card">
                    <div className="card-body">
                        <button className="btn btn-success mb-3" onClick={addComparison}>
                            <i className="fa-solid fa-plus"></i>
                            <a> Add new comparison </a>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}