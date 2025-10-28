import React, { useEffect, useRef } from 'react';
import { useTranslation } from 'react-i18next';
import { PortfolioData } from '../types';

interface MainProps {
  data: PortfolioData;
}

const Main: React.FC<MainProps> = ({ data }) => {
  const { t } = useTranslation();
  const sectionsRef = useRef<(HTMLElement | null)[]>([]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1 }
    );

    sectionsRef.current.forEach((section) => {
      if (section) {
        section.classList.add('fade-out');
        observer.observe(section);
      }
    });

    return () => observer.disconnect();
  }, [data]);

  return (
    <main>
      <h2 ref={(el) => { sectionsRef.current[0] = el; }}>{t('hello')}</h2>
      <p ref={(el) => { sectionsRef.current[1] = el; }}>{data.description}</p>
      <p ref={(el) => { sectionsRef.current[2] = el; }}>{data.current_work}</p>

      <h3 ref={(el) => { sectionsRef.current[3] = el; }}>{t('notableProjects')}</h3>
      <ul ref={(el) => { sectionsRef.current[4] = el; }}>
        {data.projects.map((project, index) => (
          <li key={index}>
            {project.link ? (
              <a href={project.link} target="_blank" rel="noopener noreferrer">
                {project.title}
              </a>
            ) : (
              project.title
            )}
            {' '}
            ({project.description})
          </li>
        ))}
      </ul>

      <h3 ref={(el) => { sectionsRef.current[5] = el; }}>{t('contact')}</h3>
      <ul ref={(el) => { sectionsRef.current[6] = el; }}>
        <li>
          {t('email')} : <a href={`mailto:${data.contact.email}`}>{data.contact.email}</a>
        </li>
        <li>
          LinkedIn : <a href={data.contact.linkedin} target="_blank" rel="noopener noreferrer">
            {data.contact.linkedin.replace('https://', '')}
          </a>
        </li>
      </ul>

      <h3 ref={(el) => { sectionsRef.current[7] = el; }}>{t('languagesTools')}</h3>
      <div className="badges" ref={(el) => { sectionsRef.current[8] = el; }}>
        {data.tools.map((tool, index) => (
          <img
            key={index}
            src={tool.badge}
            alt={tool.name}
            style={{ '--delay': `${index * 0.15}s` } as React.CSSProperties}
          />
        ))}
      </div>
    </main>
  );
};

export default Main;
