import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';
import { Button, ButtonToolbar } from 'react-bootstrap';
import { FaEdit } from 'react-icons/fa';
import { RiDeleteBin5Line } from 'react-icons/ri';
import { getDevices, deleteDevice } from '../services/DeviceService';
import AddDeviceModal from "./AddDeviceModal";
import UpdateDeviceModal from "./UpdateDeviceModal";

const Manage = () => {
    const [devices, setDevices] = useState([]);
    const [addModalShow, setAddModalShow] = useState(false);
    const [editModalShow, setEditModalShow] = useState(false);
    const [editDevice, setEditDevice] = useState([]);
    const [isUpdated, setIsUpdated] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await getDevices();
                setDevices(data);
            } catch (error) {
                console.error('Error fetching devices:', error);
            }
        };

        fetchData(); // Fetch data initially

        // Sent interval to fetch data every 10 seconds
        const interval = setInterval(fetchData, 10000); // Adjust interval as needed

        // Cleanup function to clear interval
        return () => clearInterval(interval);
    }, []);

    const handleUpdate = (e, dev) => {
        e.preventDefault();
        setEditModalShow(true);
        setEditDevice(dev);
    };

    const handleAdd = (e) => {
        e.preventDefault();
        setAddModalShow(true);
    };

    const handleDelete = (e, deviceId) => {
        if (window.confirm('Are you sure?')) {
            e.preventDefault();
            deleteDevice(deviceId)
                .then((result) => {
                    alert(result);
                    setIsUpdated(true);
                })
                .catch((error) => {
                    console.error("Failed to Delete Device:", error);
                    alert("Failed to Delete Device");
                });
        }
    };

    let AddModelClose = () => setAddModalShow(false);
    let EditModelClose = () => setEditModalShow(false);

    return (
        <div className="container-fluid side-container">
            <div className="row side-row">
                <p id="manage"></p>
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
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {devices.map((dev) => (
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
                                <td>
                                    <Button className="mr-2" variant="danger" onClick={(event) => handleDelete(event, dev.deviceId)}>
                                        <RiDeleteBin5Line />
                                    </Button>
                                    <Button className="mr-2" onClick={(event) => handleUpdate(event, dev)}>
                                        <FaEdit />
                                    </Button>
                                    <UpdateDeviceModal show={editModalShow} device={editDevice} setUpdated={setIsUpdated} onHide={EditModelClose} />
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
                <ButtonToolbar>
                    <Button variant="primary" onClick={handleAdd}>
                        Add Device
                    </Button>
                    <AddDeviceModal show={addModalShow} setUpdated={setIsUpdated} onHide={AddModelClose} />
                </ButtonToolbar>
            </div>
        </div>
    );
};

export default Manage;