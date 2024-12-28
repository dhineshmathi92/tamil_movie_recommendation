# Tamil Movie Recommendation Application

## Overview
The **Tamil Movie Recommendation Application** is a web-based platform that suggests Tamil movies to users based on their preferences. The application employs content-based recommendation techniques and fetches movie posters dynamically from IMDb for a visually appealing experience. You can access the live application here: [Tamil Movie Recommender](https://tamilmovie-recommender.streamlit.app/).

## Features
- **Content-Based Recommendations**: Suggests Tamil movies based on user-selected preferences and similar content.
- **Dynamic Poster Retrieval**: Fetches movie posters directly from IMDb using web scraping techniques.
- **Interactive Interface**: Built with Streamlit for a simple and user-friendly experience.
- **Wide Movie Coverage**: Covers a variety of Tamil movies, including classics and recent releases.

## Technologies Used
- **Content-Based Recommendation**: To identify and suggest movies with similar attributes.
- **Streamlit**: For building an interactive web application.
- **IMDb Integration**: Movie posters fetched using IMDb.
- **BeautifulSoup**: For web scraping and retrieving movie data from IMDb.

## How It Works
1. **User Input**:
   - Users select their favorite Tamil movies or genres from the interface.
2. **Recommendation Engine**:
   - The application finds similar movies based on content attributes like genre, cast, and director.
3. **Poster Retrieval**:
   - BeautifulSoup is used to scrape IMDb for movie posters, providing a visually engaging recommendation.
4. **Display**:
   - Recommendations, along with posters, are displayed in a clean and intuitive layout.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd tamil-movie-recommendation
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8501/
   ```
3. Select your favorite Tamil movies or genres to receive recommendations.

Alternatively, use the live application: [Tamil Movie Recommender](https://tamilmovie-recommender.streamlit.app/).

## Future Enhancements
- Incorporate user-based collaborative filtering for enhanced personalization.
- Add multilingual support for non-Tamil users.
- Include additional metadata like reviews and ratings in recommendations.
- Optimize the poster retrieval process to reduce latency.

