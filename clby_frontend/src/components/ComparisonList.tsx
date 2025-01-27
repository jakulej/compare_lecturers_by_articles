import 'bootstrap/dist/css/bootstrap.css';
import {useEffect, useState} from "react";
import {LecturerDTO} from "../DTOs/LecturerDTO.tsx";
import axios from "axios";
import {API_URL} from "../api/Axios.tsx";
import ComparisonComponent from "./ComparisonComponent.tsx";

export default function ComparisonList() {
    const [lecturers, setLecturers] = useState<LecturerDTO[]>([]);
    const [count, setCount] = useState(0);

    useEffect(() => {
        axios
            .get(API_URL + '...')
            .then((response) => {
                setLecturers(response.data);
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