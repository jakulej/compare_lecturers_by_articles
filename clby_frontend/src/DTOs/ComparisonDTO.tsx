import {LecturerDTO} from "./LecturerDTO.tsx";
import {ManovaResultDTO} from "./ManovaResultDTO.tsx";

export type ComparisonDTO = {
    id: number;
    lecturerlist: LecturerDTO[];
    result: ManovaResultDTO[];
}