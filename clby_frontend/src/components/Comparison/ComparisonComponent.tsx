import LecturerComponent from "../Lecturer/LecturerComponent.tsx";
import ResultComponent from "../Result/ResultComponent.tsx";

export default function ComparisonComponent (){


    return (
        <>
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
            <nav>
                <LecturerComponent/>
                <LecturerComponent/>
            </nav>
            <ResultComponent/>
        </>
    )
}