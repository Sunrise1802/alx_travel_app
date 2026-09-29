# ALX Travel App - Database Modeling and Data Seeding

## Project Description

This project is part of the ALX Backend development training.

The project focuses on building the database models and seeding sample data for a travel listing application using Django and Django REST Framework.

## Models

The application contains three main models:

### Listing

The `Listing` model represents a property available for booking.

It contains:

- Title
- Description
- Location
- Price
- Number of bedrooms
- Number of bathrooms
- Creation date

### Booking

The `Booking` model represents a booking made for a listing.

It contains:

- Listing
- Guest name
- Check-in date
- Check-out date
- Creation date

### Review

The `Review` model represents a review for a listing.

It contains:

- Listing
- Reviewer name
- Rating
- Comment
- Creation date

## Serializers

The project includes:

- `ListingSerializer`
- `BookingSerializer`

These serializers convert Django model data into a format that can be used by APIs.

## Database Seeding

A custom Django management command called `seed` has been created.

The command creates sample listing data in the database.

To run the seed command:

```bash
python manage.py seed
