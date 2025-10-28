import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  fr: {
    translation: {
      home: 'Accueil',
      cv: 'CV',
      projects: 'Projets',
      github: 'Github',
      hello: 'Bonjour ! Bienvenu sur ma page 👋',
      notableProjects: '🚀 Quelques projets marquants',
      contact: '📫 Contact',
      languagesTools: '🛠️ Langages & Outils',
      email: 'Email',
      copyright: 'Tous droits réservés.',
    }
  },
  en: {
    translation: {
      home: 'Home',
      cv: 'CV',
      projects: 'Projects',
      github: 'Github',
      hello: "Hello! Nice to meet you, I'm Lylian Challier 👋",
      notableProjects: '🚀 Notable Projects',
      contact: '📫 Contact',
      languagesTools: '🛠️ Languages & Tools',
      email: 'Email',
      copyright: 'All rights reserved.',
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'fr',
    fallbackLng: 'fr',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
