import axios from 'axios';

export const API_URL = "http://127.0.0.1:5000";

export interface CompareLecturersRequest {
    lecturer1: string;
    lecturer2: string;
}

export interface CompareLecturersResponse {
    lecturer1: string;
    lecturer2: string;
    comparison: string;
}

const axiosInstance = async (
    data: CompareLecturersRequest
): Promise<CompareLecturersResponse> => {
    try {
        const response = await axios.post<CompareLecturersResponse>(
            `${API_URL}/compare`,
            data
        );
        return response.data;
    } catch (error) {
        console.error("Error comparing lecturers:", error);
        throw error;
    }
}

export default axiosInstance;