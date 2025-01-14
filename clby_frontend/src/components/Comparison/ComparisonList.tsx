import ComparisonComponent from "./ComparisonComponent.tsx";
import 'bootstrap/dist/css/bootstrap.css';

export default function ComparisonList() {
    return (
        <div>
            <ComparisonComponent/>
            <button className="btn btn-success mb-3">
                <i className="fa-solid fa-plus"></i>
                <a> Add new goal</a>
            </button>
        </div>
    );
}