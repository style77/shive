import { config } from "process";

interface Config {
    API_URL: string;
}

const config: Config = {
    API_URL: process.env.VITE_API_URL || 'http://localhost:8000/api/v1/',
};

export default config;