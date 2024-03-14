import config from '@/config';
import errorHandler from '@/handlers/errorHandler';
import successHandler from '@/handlers/successHandler';
import axios from 'axios';


export const login = async (email: string, password: string) => {
    try {
        const response = await axios.post(
            config.API_URL + `auth/token`,
            { email, password }
        )

        const { data } = response;

        successHandler();
        return data;
    } catch (error) {
        return errorHandler()
    }
}