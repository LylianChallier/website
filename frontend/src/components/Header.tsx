import React, { useEffect, useState } from 'react';

interface HeaderProps {
  name: string;
  title: string;
}

const Header: React.FC<HeaderProps> = ({ name, title }) => {
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    setAnimate(true);
  }, []);

  return (
    <header>
      <div className="header-content">
        <h1 className={animate ? 'header-animated' : ''}>{name}</h1>
        <p>{title}</p>
      </div>
    </header>
  );
};

export default Header;
