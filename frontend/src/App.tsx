import { useEffect, useState } from 'react';
import './App.css';
import './i18n';
import { useTranslation } from 'react-i18next';
import { getPortfolioData } from './api';
import { PortfolioData } from './types';
import Header from './components/Header';
import Navigation from './components/Navigation';
import Main from './components/Main';
import Footer from './components/Footer';

function App() {
  const { i18n } = useTranslation();
  const [portfolioData, setPortfolioData] = useState<PortfolioData | null>(
    null
  );
  const [loading, setLoading] = useState(true);
  const [currentLang, setCurrentLang] = useState('fr');

  useEffect(() => {
    loadPortfolioData(currentLang);
  }, [currentLang]);

  const loadPortfolioData = async (lang: string) => {
    try {
      setLoading(true);
      const data = await getPortfolioData(lang);
      setPortfolioData(data);
    } catch (error) {
      console.error('Error loading portfolio data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLanguageChange = (lang: string) => {
    setCurrentLang(lang);
    i18n.changeLanguage(lang);
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (!portfolioData) {
    return <div className="error">Error loading portfolio data</div>;
  }

  return (
    <div className="App">
      <Header name={portfolioData.name} title={portfolioData.title} />
      <Navigation
        onLanguageChange={handleLanguageChange}
        currentLang={currentLang}
      />
      <Main data={portfolioData} />
      <Footer name={portfolioData.name} />
    </div>
  );
}

export default App;
