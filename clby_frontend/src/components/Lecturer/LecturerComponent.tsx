import {LecturerDTO} from "../../DTOs/LecturerDTO";
import {useEffect, useState} from "react";
import axios from "axios";
import {baseURL} from "../../api/Axios";
import {useParams} from "react-router";

export default function LecturerComponent () {
    const [lecturer, setLecturer] = useState<LecturerDTO | null>();
    const {id} = useParams();

    useEffect(() => {
        axios
            .get(baseURL + '...' + id) //to do!!!
            .then((response) => {
                setLecturer(response.data);
                console.log(response);
            })
            .catch(error => console.log(error));
    }, []);
    return (
        <div>
            <h1>List of Users</h1>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>id:</th>
                        <th>name:</th>
                        <th>surname:</th>
                    </tr>
                    <tbody>
                    {
                        lecturer
                            ?
                            <tr>
                                <td>{lecturer.id}</td>
                                <td>{lecturer.name}</td>
                                <td>{lecturer.surname}</td>
                            </tr>
                            : null
                    }
                    </tbody>
                    </thead>
                </table>
            </div>
        </div>
    );
}