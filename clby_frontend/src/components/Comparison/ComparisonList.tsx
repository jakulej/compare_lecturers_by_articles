import 'bootstrap/dist/css/bootstrap.css';

export default function ComparisonList() {
    return (
        <div>
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
                <div>
                    <div>
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
                        <div className="input-group mb-3">
                            <input className="form-control" list="datalistOptions" id="exampleDataList"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions">
                                <option value="Jan Kowalski1"/>
                                <option value="Jan Kowalski2"/>
                                <option value="Jan Kowalski3"/>
                                <option value="Jan Kowalski4"/>
                                <option value="Jan Kowalski5"/>
                            </datalist>
                            <input className="form-control" list="datalistOptions2" id="exampleDataList2"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions2">
                                <option value="Anna Nowak1"/>
                                <option value="Anna Nowak2"/>
                                <option value="Anna Nowak3"/>
                                <option value="Anna Nowak4"/>
                                <option value="Anna Nowak5"/>
                            </datalist>
                        </div>
                    </div>

                    <div>
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
                        <div className="input-group mb-3">
                            <input className="form-control" list="datalistOptions" id="exampleDataList"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions">
                                <option value="Jan Kowalski1"/>
                                <option value="Jan Kowalski2"/>
                                <option value="Jan Kowalski3"/>
                                <option value="Jan Kowalski4"/>
                                <option value="Jan Kowalski5"/>
                            </datalist>
                            <input className="form-control" list="datalistOptions2" id="exampleDataList2"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions2">
                                <option value="Anna Nowak1"/>
                                <option value="Anna Nowak2"/>
                                <option value="Anna Nowak3"/>
                                <option value="Anna Nowak4"/>
                                <option value="Anna Nowak5"/>
                            </datalist>
                        </div>
                    </div>

                    <div>
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
                        <div className="input-group mb-3">
                            <input className="form-control" list="datalistOptions" id="exampleDataList"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions">
                                <option value="Jan Kowalski1"/>
                                <option value="Jan Kowalski2"/>
                                <option value="Jan Kowalski3"/>
                                <option value="Jan Kowalski4"/>
                                <option value="Jan Kowalski5"/>
                            </datalist>
                            <input className="form-control" list="datalistOptions2" id="exampleDataList2"
                                   placeholder="Type to search..."/>
                            <datalist id="datalistOptions2">
                                <option value="Anna Nowak1"/>
                                <option value="Anna Nowak2"/>
                                <option value="Anna Nowak3"/>
                                <option value="Anna Nowak4"/>
                                <option value="Anna Nowak5"/>
                            </datalist>
                        </div>
                    </div>
                </div>

            </nav>
            <button className="btn btn-success mb-3">
                <i className="fa-solid fa-plus"></i>
                <a> Add new goal</a>
            </button>
        </div>
    );
}