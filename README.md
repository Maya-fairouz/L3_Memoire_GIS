#  GIS-Based Railway Management System 

A **Geographic Information System (GIS)** and **SUMO-powered** web application designed to support the management operations of Tramway.  
This project was developed as part of the **Bachelor’s Thesis (Licence 3 – 2023)** at **University Constantine 2 – AbdelHamid Mehri**.

---

##  Project Overview

This system aims to **digitalize and optimize the management of Algeria’s railway infrastructure** using GIS technology.  
The web platform provides a **centralized control interface** to monitor, analyze, and manage railway operations, including trains, maintenance, field agents, and incidents — with **real-time simulation** powered by **SUMO**.

It replicates the functions of a **Central Control Panel (CCP)** for real-time supervision, route monitoring, and maintenance coordination.

---

##  Objectives

- Design and implement a **GIS-based management platform** for SETRAM.  
- Simulate and visualize **train movement** using **SUMO** (Simulation of Urban MObility).  
- Manage railway assets, incidents, obstacles, and maintenance teams.  
- Improve **decision-making**, **safety**, and **operational efficiency**.  
- Provide an **interactive dashboard** for different managerial roles.

---

## System Actors

| Actor | Description | Main Responsibilities |
|-------|--------------|------------------------|
| **Operation Manager** | Oversees entire operations | Monitor traffic, consult maps, respond to incidents |
| **Depot Manager** | Manages depots & maintenance teams | Schedule maintenance, manage staff, generate reports |
| **Train Controller** | Manages train movements | Create/update schedules, report incidents, monitor network |
| **Team Manager** | Supervises field maintenance teams | Assign tasks, track progress, manage work orders |
| **Field Agent** | Reports on-site conditions | Report obstacles, send updates, communicate with HQ |

---

## Features

 Interactive GIS dashboard (Leaflet/Folium)  
 SUMO-driven train and vehicle simulation  
 Role-based authentication and dashboards  
 Incident and maintenance management  
 Notification and communication system  
 Real-time location monitoring  
 Database schema with agents, trains, incidents, maintenance, obstacles, and notifications  

---

##  Technologies Used

| Category | Technology |
|-----------|-------------|
| **Framework** | Django 4.x |
| **Language** | Python, JavaScript, HTML, CSS |
| **Database** | PostgreSQL / SQLite |
| **Simulation Engine** | SUMO (Simulation of Urban MObility) |
| **GIS / Mapping** | Leaflet + Folium |
| **Frontend UI** | Bootstrap 5 |
| **Development Tools** | VS Code, Draw.io |
| **Data Formats** | JSON, XML, SQL |
