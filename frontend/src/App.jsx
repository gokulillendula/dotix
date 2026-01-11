import { useEffect, useState } from "react"
import { api } from "./api"
import "./App.css"

export default function App() {
  const [jobs, setJobs] = useState([])
  const [taskName, setTaskName] = useState("")
  const [priority, setPriority] = useState("Low")
  const [payload, setPayload] = useState("")

  const fetchJobs = async () => {
    const res = await api.get("/jobs/list")
    setJobs(res.data)
  }

const createJob = async () => {
  let parsed = {}

  try {
    parsed = JSON.parse(payload)
  } catch {
    alert("Invalid JSON payload")
    return
  }

  try {
    await api.post("/jobs", {
      taskName,
      priority,
      payload: parsed
    })
    fetchJobs()
  } catch (err) {
    console.log("Django error:", err.response.data)
    alert(JSON.stringify(err.response.data))
  }
}



  const runJob = async (id) => {
    await api.post(`/run-job/${id}`)
    fetchJobs()
  }
const deleteJob = async (id) => {
  await api.delete(`/jobs/delete/${id}`)
  fetchJobs()
}

useEffect(() => {
  fetchJobs()
  const interval = setInterval(fetchJobs, 2000) // every 2 seconds
  return () => clearInterval(interval)
}, [])


  return (
    <div className="container">
      <h1>Dotix Automation Dashboard</h1>

      <div className="card form">
        <input placeholder="Task Name" onChange={e=>setTaskName(e.target.value)} />
        <select onChange={e=>setPriority(e.target.value)}>
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>
        <textarea placeholder='{"email":"test@gmail.com"}' onChange={e=>setPayload(e.target.value)} />
        <button onClick={createJob}>Create Job</button>
      </div>
      <div className="card">
      <table>
        <thead>
          <tr>
            <th>Task</th><th>Priority</th><th>Status</th><th>Run</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map(job => (
            <tr key={job.id}>
              <td>{job.taskName}</td>
              <td>
                <span className={`priority ${job.priority}`}>
                  {job.priority}
                </span>
              </td>

              <td>
                <span className={`status ${job.status}`}>
                  {job.status}
                </span>
              </td>

              <td>
                <button className="action-btn run-btn" onClick={()=>runJob(job.id)}>
                  Run
                </button>

                <button className="action-btn delete-btn" onClick={()=>deleteJob(job.id)}>
                  Delete
                </button>
              </td>

            </tr>
          ))}
        </tbody>
      </table>
      </div>

    </div>
  )
}
