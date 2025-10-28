import axios from 'axios';
import { PortfolioData } from './types';

const API_BASE_URL = 'http://localhost:8000/api';

export const getPortfolioData = async (
  lang: string = 'fr'
): Promise<PortfolioData> => {
  const response = await axios.get(`${API_BASE_URL}/portfolio/`, {
    params: { lang },
  });
  return response.data;
};
