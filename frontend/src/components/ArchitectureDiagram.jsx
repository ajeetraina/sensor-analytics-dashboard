import React, { useEffect } from 'react';
import mermaid from 'mermaid';

const ArchitectureDiagram = () => {
  useEffect(() => {
    mermaid.initialize({
      startOnLoad: true,
      theme: 'neutral',
      securityLevel: 'loose',
      flowchart: { useMaxWidth: false }
    });
    
    // Render all mermaid diagrams
    mermaid.contentLoaded();
  }, []);

  const diagramDefinition = `
    graph TB
      subgraph Frontend["Frontend (Next.js + Vite)"]
        UI["React UI"] --> Charts["Recharts Visualizations"]
        UI --> WebSocket["WebSocket Client"]
        UI --> REST["REST API Client"]
      end

      subgraph Backend["Backend (Python)"]
        Flask["Flask Server"] --> SocketIO["Socket.IO Server"]
        Flask --> APIRoutes["REST API Routes"]
        SocketIO --> DataProcessor
        APIRoutes --> DataProcessor["Data Processor"]
        DataProcessor --> Neo4jConnector["Neo4j Connector"]
      end

      subgraph Database["Neo4j Graph Database"]
        GraphData["Sensor Graph Data"]
        Classifications["Classification Nodes"]
        TimeGroups["Time Group Nodes"]
        Relations["Relationships"]
      end

      WebSocket <--> SocketIO
      REST <--> APIRoutes
      Neo4jConnector <--> GraphData
      Neo4jConnector <--> Classifications
      Neo4jConnector <--> TimeGroups
      Neo4jConnector <--> Relations

      style Frontend fill:#d4f1f9,stroke:#87CEEB
      style Backend fill:#d5f5e3,stroke:#82E0AA
      style Database fill:#fcf3cf,stroke:#F4D03F
  `;

  return (
    <div className="bg-white p-6 rounded-lg shadow mb-6">
      <h2 className="text-2xl font-semibold mb-4">Architecture Diagram</h2>
      <div className="mermaid overflow-auto">
        {diagramDefinition}
      </div>
    </div>
  );
};

export default ArchitectureDiagram;
