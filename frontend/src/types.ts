export interface Project {
  title: string;
  description: string;
  link?: string;
}

export interface Contact {
  email: string;
  linkedin: string;
}

export interface Tool {
  name: string;
  badge: string;
}

export interface PortfolioData {
  name: string;
  title: string;
  description: string;
  current_work: string;
  projects: Project[];
  contact: Contact;
  tools: Tool[];
}
