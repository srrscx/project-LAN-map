import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import { getDevices } from '../services/DeviceService';
import "../App.css";

const Devices = () => {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    // Function to fetch devices data
    const fetchDevicesData = async () => {
      try {
        const data = await getDevices();
        setDevices(data);
      } catch (error) {
        console.error('Error fetching devices:', error);
      }
    };

    // Fetch devices data initially
    fetchDevicesData();

    // Set interval to fetch devices data every 5 seconds (for example)
    const interval = setInterval(fetchDevicesData, 5000); // 5000 milliseconds = 5 seconds

    // Clean up function to clear interval
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container-fluid side-container">
      <div className="row side-row" >
        <p id="before-table"></p>
        <Table striped bordered hover className="react-bootstrap-table" id="dataTable">
          <thead>
            <tr>
              <th>ID</th>
              <th>Device Name</th>
              <th>IP Address</th>
              <th>MAC Address</th>
              <th>Device Type</th>
              <th>Building</th>
              <th>Floor</th>
              <th>Department</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {devices.map((dev) =>
              <tr key={dev.id}>
                <td>{dev.deviceId}</td>
                <td>{dev.deviceName}</td>
                <td>{dev.ip_address}</td>
                <td>{dev.mac_address}</td>
                <td>{dev.deviceType}</td>
                <td>{dev.building}</td>
                <td>{dev.floor}</td>
                <td>{dev.department}</td>
                <td>{dev.status}</td>
              </tr>
            )}
          </tbody>
        </Table>
      </div>
    </div>
  );
};

export default Devices;