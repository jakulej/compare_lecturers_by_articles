import {useEffect, useState} from "react";
import axios from "axios";
import {baseURL} from "../../api/Axios";
import {useParams} from "react-router";
import {ManovaResultDTO} from "../../DTOs/ManovaResultDTO.tsx";

export default function ResultComponent() {
    const [result, setResult] = useState<ManovaResultDTO | null>();
    const {id} = useParams();

    useEffect(() => {
        axios
            .get(baseURL + '...' + id) //to do!!!
            .then((response) => {
                setResult(response.data);
                console.log(response);
            })
            .catch(error => console.log(error));
    }, []);

    return (
        <>
            <h1>Result</h1>
            <div>
                <table>
                    <thead>
                    <tr>
                        <th>id:</th>
                        <th>Wilks' lambda:</th>
                        <th>Pillai's trace:</th>
                        <th>Hotelling-Lawley trace:</th>
                        <th>Roy's greatest root:</th>
                    </tr>
                    <tbody>
                    {
                        result
                            ?
                            <tr>
                                <td>{result.id}</td>
                                <td>{result.wilksLambda}</td>
                                <td>{result.pillaisTrace}</td>
                                <td>{result.hotellingLawleyTrace}</td>
                                <td>{result.roysGreatestRoot}</td>
                            </tr>
                            : null
                    }
                    </tbody>
                    </thead>
                </table>
            </div>
        </>
    );
}