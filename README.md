@Author: Saurabh
# BookHub

BookHub is a community-driven platform focused on sharing and exploring book recommendations. The platform integrates with the Google Books API to fetch book data and allows users to submit their own recommendations, interact with others.

## Features

1. **Integration with Google Books API**
   - Search for books by title, author, or keywords.
   - Fetch and display book details including title, author, description, cover image, and ratings.

2. **Community Book Recommendations**
   - Users can submit their own book recommendations.
   - API endpoints to manage recommendations, including likes, comments, and filtering by genre, rating, and publication date.
   - Dynamic frontend for browsing and interacting with recommendations.

3. **Developer API Guide**
   - Comprehensive guide for developers to create custom API endpoints for additional book-related functionalities.

## Installation

### Prerequisites
- Python 3.11
- Django 5.0.7
- pip (Python package installer)
- Google Books API Key (Optional)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SaurabhSinghal579/Book-Hub.git
   cd BookHub

2. **Setup Environment Variables**
    GOOGLE_BOOKS_API_KEY=YOUR GOOGLE BOOK API KEY

3. **Run Server**
    python manage.py runserver

    - Access the application at http://127.0.0.1:8000/recommendations/search/
    - Give the new recommendation at http://127.0.0.1:8000/recommendations/submit_recommendations/
    - View all recommendations at http://127.0.0.1:8000/recommendations/recommendations/
    - Acces Django Admin at http://127.0.0.1:8000/admin/recommendations/
        *credential for Django admin: username- test
                                      password- 1234 