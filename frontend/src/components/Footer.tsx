import React from 'react';
import { useTranslation } from 'react-i18next';

interface FooterProps {
  name: string;
}

const Footer: React.FC<FooterProps> = ({ name }) => {
  const { t } = useTranslation();

  return (
    <footer>
      &copy; 2025 {name}. {t('copyright')}
    </footer>
  );
};

export default Footer;
