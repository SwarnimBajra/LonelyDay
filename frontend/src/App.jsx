import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [userInput, setUserInput] = useState("");
  const [emotionResult, setEmotionResult] = useState(null);
  const [error, setError] = useState("");
  const [graphUrl, setGraphUrl] = useState("");

  // Handle input change
  const handleChange = (e) => {
    setUserInput(e.target.value);
  };

  // Handle form submission for emotion detection
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setEmotionResult(null);

    console.log("userin: ", userInput)

    try {
      const response = await axios.post("http://127.0.0.1:8000/analyze-emotion", {
        text: userInput,
      });

      setEmotionResult(response.data);
      setUserInput(""); // Clear input field
    } catch (err) {
      setError("An error occurred while analyzing the emotion.");
      console.error(err);
    }
  };

  // Handle graph generation
  const generateGraph = async () => {
    setError("");
    setGraphUrl("");

    try {
      const response = await axios.get("http://127.0.0.1:8000/generate-graph", {
        responseType: "blob",
      });

      // Convert Blob to a URL for display
      const url = URL.createObjectURL(new Blob([response.data]));
      setGraphUrl(url);
    } catch (err) {
      setError("An error occurred while generating the graph.");
      console.error(err);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Emotion Detection</h1>

      {/* Emotion Detection Form */}
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          value={userInput}
          onChange={handleChange}
          placeholder="Enter text to analyze..."
          style={styles.input}
        />
        <button type="submit" style={styles.button}>
          Analyze Emotion
        </button>
      </form>

      {/* Emotion Result */}
      {emotionResult && (
        <div style={styles.result}>
          <h3>Detected Emotion: {emotionResult.emotion}</h3>
          <p>Confidence Score: {emotionResult.score.toFixed(4)}</p>
        </div>
      )}

      {/* Error Message */}
      {error && <p style={styles.error}>{error}</p>}

      {/* Generate Graph Button */}
      <button onClick={generateGraph} style={styles.button}>
        Generate Emotion Graph
      </button>

      {/* Display Graph */}
      {graphUrl && (
        <div style={styles.graphContainer}>
          <h3>Emotion Graph</h3>
          <img src={graphUrl} alt="Emotion Graph" style={styles.graphImage} />
        </div>
      )}
    </div>
  );
};

const styles = {
  container: {
    textAlign: "center",
    padding: "20px",
    fontFamily: "'Arial', sans-serif",
  },
  title: {
    fontSize: "2rem",
    color: "#333",
  },
  form: {
    margin: "20px 0",
  },
  input: {
    padding: "10px",
    fontSize: "1rem",
    marginRight: "10px",
    width: "300px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "1rem",
    backgroundColor: "#4CAF50",
    color: "#fff",
    border: "none",
    cursor: "pointer",
    borderRadius: "5px",
  },
  result: {
    marginTop: "20px",
    fontSize: "1.2rem",
  },
  error: {
    color: "red",
    marginTop: "10px",
  },
  graphContainer: {
    marginTop: "20px",
  },
  graphImage: {
    width: "100%",
    maxWidth: "600px",
    borderRadius: "10px",
    marginTop: "10px",
  },
};

export default App;
