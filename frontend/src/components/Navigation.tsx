import React from 'react';
import { useTranslation } from 'react-i18next';

interface NavigationProps {
  onLanguageChange: (lang: string) => void;
  currentLang: string;
}

const Navigation: React.FC<NavigationProps> = ({ onLanguageChange, currentLang }) => {
  const { t } = useTranslation();

  return (
    <nav>
      <div className="nav-left">
        <a href="/">{t('home')}</a>
        <a href="/media/CV.pdf" target="_blank" rel="noopener noreferrer">{t('cv')}</a>
        <a href="/projects">{t('projects')}</a>
        <a href="https://github.com/lylianchallier" target="_blank" rel="noopener noreferrer">{t('github')}</a>
      </div>
      <div className="lang-switcher">
        <button
          onClick={() => onLanguageChange('fr')}
          title="Français"
          className={currentLang === 'fr' ? 'active' : ''}
          aria-label="Changer la langue en français"
        >
          <img src="https://flagcdn.com/fr.svg" alt="Français" width="24" />
        </button>
        <button
          onClick={() => onLanguageChange('en')}
          title="English"
          className={currentLang === 'en' ? 'active' : ''}
          aria-label="Change language to English"
        >
          <img src="https://flagcdn.com/gb.svg" alt="English" width="24" />
        </button>
      </div>
    </nav>
  );
};

export default Navigation;
