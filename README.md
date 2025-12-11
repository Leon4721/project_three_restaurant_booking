# Café Central – Restaurant Booking System

Café Central is a full-stack restaurant booking application built with Django and Python. Guests can create, edit, and cancel table reservations using a unique booking code, while staff can manage bookings securely via the Django admin and a staff login route.

The project demonstrates full CRUD functionality, relational database design, form validation, and deployment to a live server.

---

## Live Project

* **Live Site:** [https://project-three-restaurant-booking.onrender.com/](https://project-three-restaurant-booking.onrender.com/)


---

## Contents

* [Project Rationale](#project-rationale)
* [Project Goals](#project-goals)

  * [User Goals](#user-goals)
  * [Site Owner Goals](#site-owner-goals)
  * [Development Goals](#development-goals)
* [User Experience (UX)](#user-experience-ux)

  * [Target Audience](#target-audience)
  * [User Stories](#user-stories)
* [Design](#design)

  * [Wireframes](#wireframes)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [UX Design Principles](#ux-design-principles)
* [Features](#features)

  * [Existing Features](#existing-features)
  * [Future Enhancements](#future-enhancements)
* [Database Design](#database-design)

  * [Data Schema](#data-schema)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Data Models](#data-models)
* [Technologies Used](#technologies-used)

  * [Languages](#languages)
  * [Frameworks and Libraries](#frameworks-and-libraries)
  * [Database](#database)
  * [Tools](#tools)
* [Testing](#testing)

  * [Manual Testing](#manual-testing)
  * [Code Validation](#code-validation)
  * [Responsive Testing](#responsive-testing)
  * [Accessibility Testing](#accessibility-testing)
  * [Bug Tracking](#bug-tracking)
* [Deployment](#deployment)

  * [Local Development](#local-development)
  * [Render Deployment](#render-deployment)
  * [Environment Variables](#environment-variables)
* [Security Features](#security-features)
* [Credits](#credits)

---

## Project Rationale

### Why Café Central Exists

Many small restaurants still rely on phone calls, paper diaries, or basic spreadsheets to manage reservations. This makes it easy to:

* Double-book tables
* Lose bookings completely
* Allow customers to book at times the restaurant is closed
* Offer a poor user experience where customers have to call during specific hours

### The Problem

* Customers expect **online self-service bookings** that work 24/7.
* Owners need to **avoid double bookings** and respect table capacities.
* Staff need a quick way to **find, edit, or cancel reservations** when customers call.
* Manual systems are error-prone and time-consuming.

### The Solution

Café Central provides a simple, mobile-friendly booking flow where users can:

* Select a **date, time, party size and table type**
* Receive a **unique booking code** on confirmation
* Use that code to **view, edit, or cancel** their booking
* Be prevented from booking **in the past** or exceeding table capacity

Meanwhile, the site owner can:

* View all bookings in the **Django admin**
* Filter by date/time and manage capacity
* Ensure bookings are stored in a **relational database** with referential integrity

### Educational Context

This project was developed as part of the **Level 5 Diploma in Web Application Development (Unit 3: Back End Development)** and demonstrates:

* Django models and relational database design
* CRUD operations and form validation
* Secure staff authentication and admin access
* Professional deployment to a live environment (Render)

[↑ Back to Top](#contents)

---

## Project Goals

### User Goals

Users want to:

* Quickly reserve a table online without calling the restaurant
* Choose a **suitable time, date, and party size**
* See immediate feedback when their booking is confirmed
* Receive a **clear booking code** they can use later
* Edit or cancel their booking if plans change
* Feel confident that **their data is handled securely**

### Site Owner Goals

The site owner wants to:

* **Automate bookings** to reduce phone calls and manual diary entries
* Avoid **double bookings** and over-capacity tables
* Keep all bookings in a **consistent, queryable database**
* Allow staff to **look up and edit bookings** quickly
* Demonstrate back-end development skills using **Django and relational databases**
* Present a professional, responsive, and accessible interface

### Development Goals

This project aims to demonstrate:

* ✅ Full-stack Django application with templates, views, and models
* ✅ **Relational database** design with at least one **ForeignKey relationship**
* ✅ Complete **CRUD**: create, read, update, delete bookings
* ✅ Secure **staff login** using Django’s authentication
* ✅ Robust **form validation** (e.g. no bookings in the past)
* ✅ Clear **user flows** with success and error messages
* ✅ **Live deployment** with environment variables and debug off in production
* ✅ Code structured in a way that is maintainable and clearly documented

[↑ Back to Top](#contents)

---

## User Experience (UX)

### Target Audience

**Primary audience**

* Diners aged 18–65 looking to reserve a restaurant table
* Users who expect a simple, no-account booking experience
* Mobile-first users who book on the go

**Secondary audience**

* Restaurant staff who need to look up, modify or cancel bookings
* Course assessors reviewing the project for Unit 3 (Back End)

### User Needs

The target audience needs:

* **Fast booking** with minimal required fields
* **Responsive design** that works on phones, tablets, and desktops
* Clear **confirmation and booking code**
* Ability to **change or cancel** a booking
* Clear error messaging if something goes wrong

### User Stories

**First-Time Visitor**

* As a first-time visitor, I want to understand immediately that this site is for **booking a table**.
* As a first-time visitor, I want to **submit a booking form quickly** without creating an account.
* As a first-time visitor, I want to be told clearly if there are **errors in my form inputs**.
* As a first-time visitor, I want to see a **clear confirmation** that my booking has been saved and a **booking code** I can keep.

**Returning User**

* As a returning user, I want to **find my booking using a booking code** so I don’t have to remember all my details.
* As a returning user, I want to **edit my booking** (date/time/party size) if my plans change.
* As a returning user, I want to **cancel my booking** easily if I can’t attend.

**Site Administrator / Staff**

* As staff, I want to **log in securely** and access the Django admin.
* As staff, I want to **view a list of all bookings** ordered by date/time.
* As staff, I want to see **table capacity and party size** to ensure no over-bookings.
* As staff, I want to be able to **edit or delete bookings** on behalf of customers.

[↑ Back to Top](#contents)

---

## Design

### Wireframes

Wireframes were created using **Balsamiq** following a **mobile-first** approach.

**Mobile (320–767px)**

* Single-column layout
* Booking form stacked vertically with large touch targets
* “Manage booking” section positioned below the main form
* Clear success and error alerts using bootstrap-style banners

**Tablet (768–1023px)**

* Two-column layout: booking form on the left, booking information / hero text on the right
* Larger inputs and more breathing space

**Desktop (1024px+)**

* Centered booking card with hero section
* Consistent navigation and footer
* Enough white space to keep the layout clean and readable

> Wireframe screenshots (mobile / tablet / desktop) are included in the `/docs` folder and referenced in the Testing/README where appropriate.

### Color Scheme

Café Central uses a clean, modern palette suitable for a restaurant brand:

| Role             | Colour (HEX) | Usage                             |
| ---------------- | ------------ | --------------------------------- |
| Primary          | `#8B4513`    | Buttons, accents, headings        |
| Secondary        | `#F5DEB3`    | Background highlights, hero areas |
| Dark Text        | `#222222`    | Main text                         |
| Light Background | `#FFFFFF`    | Card backgrounds, forms           |
| Alert Success    | `#198754`    | Success messages                  |
| Alert Danger     | `#DC3545`    | Error / validation messages       |

Colours were chosen to:

* Suggest warmth and coffee/restaurant tones
* Maintain adequate contrast for readability
* Keep the UI simple and professional for assessment

### Typography

A system font stack is used for performance and familiarity:

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
             "Helvetica Neue", Arial, sans-serif;
```

* **Headings:** Bold / semi-bold
* **Body text:** Regular 16px minimum
* **Buttons & Labels:** Semi-bold for emphasis

Line height of **1.4–1.6** is used to keep text legible on all screen sizes.

### UX Design Principles

The design follows key UX principles:

1. **Clarity**

   * Single primary action on the home page: **book a table**.
   * Manage booking, edit and cancel flows are clearly labelled.

2. **Feedback**

   * Success and error messages displayed using Bootstrap-style alerts.
   * Invalid fields are highlighted with helpful messages.

3. **Consistency**

   * Form layout is consistent across create, edit, and manage views.
   * Buttons share common styling (colour, hover states).

4. **Accessibility**

   * Labels associated with all form inputs.
   * Colour contrast considered for text and buttons.
   * Logical heading order and semantic HTML where possible.

5. **Mobile-First**

   * Layout is designed to work on small screens first.
   * Larger screens enhance spacing and layout but do not change the core flow.

[↑ Back to Top](#contents)

---

## Features

### Existing Features

1. **Home Page – Make a Booking**

   * Single, intuitive form to create a booking.
   * Fields typically include:

     * Name
     * Email
     * Phone
     * Date
     * Time
     * Number of guests
     * Table type / location (e.g. window, booth, main floor)
   * Server-side validation ensures:

     * All required fields are completed
     * Guests do not exceed the maximum capacity
     * **Dates in the past cannot be booked**

2. **Unique Booking Code Generation**

   * Each booking is assigned a **unique booking code** (UUID).
   * On successful submission:

     * A success message is shown
     * The booking code is clearly displayed to the user
   * This code is used later to **manage, edit, or cancel** the booking.

3. **Manage Booking**

   * Dedicated “Manage booking” section or page.
   * Users can enter their **booking code** (and optionally email) to retrieve their booking.
   * If the code is valid:

     * Booking details are displayed
     * Links/buttons are provided to **edit** or **cancel** the booking

4. **Edit Booking**

   * Users can update:

     * Date
     * Time
     * Number of guests
     * Table choice
   * The same validation rules apply:

     * No past dates
     * Capacity limits respected
   * On success, a confirmation message is displayed and the user can see the updated booking.

5. **Cancel Booking**

   * Users can cancel their booking from the manage view.
   * Confirmation flow prevents accidental cancellations.
   * Canceled bookings are removed (or flagged) in the database.

6. **Staff Login and Django Admin**

   * A **staff login link** enables staff to sign in with Django authentication.
   * Staff users (with `is_staff=True`) can access the **Django admin panel** to:

     * View all bookings
     * Filter by date/time/table
     * Edit or delete bookings as needed
   * Only authenticated staff can access the admin area.

7. **Validation and Error Handling**

   * Form errors are displayed near the relevant fields.
   * Global error messages appear for invalid booking codes or missing records.
   * Server-side validation prevents bypassing rules such as:

     * Booking dates in the past
     * Exceeding table capacity

8. **Responsive Layout**

   * Uses a responsive layout (Bootstrap-style grid and utility classes).
   * Tested on multiple screen sizes to avoid horizontal scrolling.

### Future Enhancements

Planned improvements that could move the project further towards Distinction level:

* **Email Confirmation:** Send a confirmation email with booking details and code.
* **User Accounts (Optional):** Allow frequent diners to register and see a history of their bookings.
* **Table View for Staff:** Custom staff dashboard showing tables and times in a visual grid.
* **Holiday / Closed Dates:** Prevent bookings on days when the restaurant is closed.
* **Automated Tests:** Django TestCase classes to cover models, forms, and views.

[↑ Back to Top](#contents)

---

## Database Design

### Data Schema

Café Central uses a **relational database** with clearly defined relationships between entities. This meets the requirement for relational data rather than a single flat table.

### Entity Relationship Diagram

Core entities:

* **Table** – physical table in the restaurant
* **Booking** – reservation made by a customer

Relationships:

* **Table → Booking (One-to-Many):**

  * One table can have many bookings over time
  * Each booking is linked to exactly one table

### Data Models

> **Note:** Field names shown here reflect the conceptual design. The actual implementation may use slightly different names or types but follows the same structure.

#### Table Model

Represents each physical table in the restaurant.

* `id` – Primary key
* `name` – Human-readable label (e.g. “Window 1”, “Booth A”)
* `capacity` – Maximum number of guests for the table
* `location` – Choice field (e.g. WINDOW, BOOTH, MAIN_FLOOR)
* `is_active` – Boolean to allow disabling a table without deleting it

**Key points:**

* Normalizes repeated data (capacity, location) instead of storing as plain text on each booking.
* Makes it easier to adjust capacity or remove tables in the future.

#### Booking Model

Represents a customer’s reservation.

* `id` – Primary key
* `booking_code` – UUID, unique code given to the user
* `customer_name` – Name of the guest
* `email` – Contact email
* `phone` – Contact number
* `date` – Date of booking
* `time` – Time of booking
* `guests` – Number of guests
* `table` – ForeignKey → `Table` (on_delete=PROTECT)
* `special_requests` – Optional text field for dietary needs, celebrations, etc.
* `created_at` – Date/time created (auto-add)
* `updated_at` – Date/time updated (auto-now)

**Constraints & Validation:**

* `booking_code` unique
* `date` not allowed in the past (validated in form or model)
* `guests` must be positive and cannot exceed `table.capacity`

**Why PROTECT on delete?**

* `on_delete=models.PROTECT` prevents deleting a table if bookings reference it, which protects historical booking data and integrity.

[↑ Back to Top](#contents)

---

## Technologies Used

### Languages

* **Python** – Back-end logic and Django framework
* **HTML5** – Templating and page structure
* **CSS3** – Styling and layout
* **JavaScript (minimal)** – Minor enhancements (if used)

### Frameworks and Libraries

* **Django 6** – Main web framework, ORM, templating, authentication
* **Bootstrap 5** (or similar) – Responsive grid and UI components
* **Gunicorn** – WSGI server for production
* **Whitenoise** – Static files handling (if configured)

### Database

* **SQLite3** – Development database
* **PostgreSQL** (typical on Render) – Production database

### Tools

* **Visual Studio Code** – Code editor
* **Git & GitHub** – Version control and repository hosting
* **Balsamiq** – Wireframe design
* **Render** – Hosting platform for deployment
* **Chrome DevTools** – Debugging and responsive testing
* **W3C Validators** – HTML and CSS validation
* **PEP8 / Flake8** – Python style and linting (where applied)

[↑ Back to Top](#contents)

---

## Testing

### Testing Strategy

The project currently relies on **comprehensive manual testing** backed by framework-level protections (Django forms, model validation, authentication).

Automated tests are considered a future enhancement.

### Manual Testing

Below is a selection of the key manual test cases performed. (You can expand this into a full table for each page.)

#### Booking Flow

| Test Case                  | Steps                                     | Expected Result                                              | Status |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------------ | ------ |
| Create booking (valid)     | Fill form with valid data and submit      | Booking created, success message shown, booking code visible | ✅      |
| Create booking (past date) | Select yesterday’s date and submit        | Form rejected, error message shown near date field           | ✅      |
| Missing required field     | Leave name empty and submit               | Form rejected, “This field is required” error shown          | ✅      |
| Max capacity exceeded      | Choose table then enter guests > capacity | Form rejected, validation message about capacity             | ✅      |

#### Manage / Edit / Cancel Booking

| Test Case                    | Steps                                   | Expected Result                                  | Status |
| ---------------------------- | --------------------------------------- | ------------------------------------------------ | ------ |
| Find booking with valid code | Enter valid booking code in manage form | Booking details displayed                        | ✅      |
| Invalid booking code         | Enter random / non-existent code        | Error message: booking not found                 | ✅      |
| Edit booking (valid change)  | Change time and submit                  | Updated booking shown, success message displayed | ✅      |
| Edit booking to past date    | Edit date to earlier than today         | Validation error for date                        | ✅      |
| Cancel booking               | Click cancel → confirm                  | Booking removed and feedback message displayed   | ✅      |

#### Staff / Admin

| Test Case              | Steps                                        | Expected Result                            | Status |
| ---------------------- | -------------------------------------------- | ------------------------------------------ | ------ |
| Staff login (valid)    | Use staff credentials at staff login / admin | Login successful, admin dashboard shown    | ✅      |
| Staff login (invalid)  | Use wrong password                           | Login page re-displayed with error message | ✅      |
| Non-staff access admin | Attempt `/admin/` as anonymous user          | Redirected to login                        | ✅      |

### Code Validation

> You can run these tools and then update the summary if anything changes.

* **HTML** – Checked with [W3C Markup Validation Service]; any critical errors fixed.
* **CSS** – Checked with [W3C CSS Validator]; minor warnings (e.g. vendor prefixes) accepted.
* **Python** – Checked with `flake8` where possible; no major PEP8 violations remaining in core files.

### Responsive Testing

Tested using Chrome DevTools and (where possible) real devices.

**Devices / widths tested:**

* iPhone SE / small mobile (320px)
* Standard modern mobile (375–414px)
* iPad / tablet (768–1024px)
* Laptop (1366–1440px)
* Desktop (1920px)

**Verified:**

* No horizontal scrolling
* Forms usable on all screen sizes
* Buttons and links large enough for touch interaction

### Accessibility Testing

* Manual checks:

  * Labels attached to inputs
  * Headings follow a logical order
  * Colour contrast checked with online tools
* WAVE / Lighthouse (run via browser extensions) used to check for obvious accessibility problems and contrast issues.

[↑ Back to Top](#contents)

---

## Bug Tracking

Below are some key issues encountered and resolved during development.

### BUG-001: 404 on Manage Booking URL

**Symptom:**
Clicking a manage/edit link produced a 404 error.

**Cause:**
The URL pattern expected `edit/<str:booking_code>/` but links/forms were pointing to a different path (`manage/<code>/`).

**Fix:**

* Updated URL patterns in `booking_app/urls.py` to match the views.
* Ensured all templates use `{% url 'edit_booking' booking.booking_code %}` and `{% url 'manage_booking' %}` consistently.

---

### BUG-002: `get_object_or_404` NameError

**Symptom:**
Django error: `NameError: name 'get_object_or_404' is not defined` in the edit view.

**Cause:**
`get_object_or_404` was used in `views.py` but not imported.

**Fix:**

* Added `from django.shortcuts import get_object_or_404` at the top of `views.py`.
* Retested edit flow – bookings now load correctly.

---

### BUG-003: Staff Login TemplateDoesNotExist

**Symptom:**
Visiting `/staff-login/` raised `TemplateDoesNotExist: booking_app/login.html`.

**Cause:**
The view was pointing to `booking_app/login.html` but the template either didn’t exist or lived in the wrong folder.

**Fix:**

* Created `booking_app/login.html` extending `base.html`.
* Ensured `TEMPLATES` configuration and app directories were correct.
* Verified login page loads without error.

---

### BUG-004: Users Could Book Past Dates

**Symptom:**
Before adding validation, users could select dates in the past.

**Cause:**
Initial implementation only used HTML `min` attributes or no validation at all.

**Fix:**

* Added server-side validation in the form/model (e.g. custom `clean_date` method).
* Prevented clients from bypassing validation by disabling JavaScript.

[↑ Back to Top](#contents)

---

## Deployment

### Local Development

#### Prerequisites

* Python 3.11+ (or 3.13 as used on Render)
* Git
* Virtual environment tool (e.g. `venv`)

#### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Leon4721/project_three_restaurant_booking.git
   cd project_three_restaurant_booking
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file (or use environment variables) with at least:

   ```text
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (for admin)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit: `http://127.0.0.1:8000/`
   Admin: `http://127.0.0.1:8000/admin/`

---

### Render Deployment

The project is deployed on **Render**.

High-level steps:

1. **Push to GitHub**

   Make sure all code is committed and pushed to the `main` branch.

2. **Create a New Web Service in Render**

   * Connect Render to your GitHub repository
   * Choose the repo: `project_three_restaurant_booking`
   * Set build command (e.g. `pip install -r requirements.txt`)
   * Set start command (e.g. `gunicorn restaurant_project.wsgi`)

3. **Configure Environment Variables in Render**

   * `SECRET_KEY` – production secret key
   * `DEBUG=False`
   * `ALLOWED_HOSTS=your-render-url.onrender.com`
   * `DATABASE_URL` – connection URL for Render’s PostgreSQL (if used)

4. **Run Migrations on Render**

   Use Render’s shell or a deployment hook to run:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Verify Deployment**

   * Visit the live URL
   * Confirm static files load correctly
   * Test booking, manage, edit, cancel flows
   * Confirm admin access works and `DEBUG=False` is respected

[↑ Back to Top](#contents)

---

## Environment Variables

Key environment variables used:

| Variable        | Description                       | Example                                 |
| --------------- | --------------------------------- | --------------------------------------- |
| `SECRET_KEY`    | Django secret key                 | `django-insecure-...`                   |
| `DEBUG`         | Debug mode flag                   | `True` (dev) / `False` (prod)           |
| `DATABASE_URL`  | Database connection string        | `sqlite:///db.sqlite3` or Postgres URL  |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames | `localhost,127.0.0.1,project-three-...` |

`.env` file should be:

* Present locally for development
* **Excluded from Git** via `.gitignore`
* Re-created via Render’s web UI for production

[↑ Back to Top](#contents)

---

## Security Features

Café Central follows Django security best practices:

1. **Authentication & Authorization**

   * Staff authentication via Django’s built-in system
   * Only authenticated staff can access `/admin/`
   * Staff accounts created via `createsuperuser`

2. **CSRF Protection**

   * CSRF tokens used on all POST forms
   * Enabled by default via Django middleware

3. **Password Security**

   * Passwords hashed using Django’s default password hasher
   * Never stored in plain text

4. **Input Validation**

   * Django forms and model validators ensure safe, cleaned input
   * Past dates and invalid capacities rejected

5. **Environment-Based Configuration**

   * `DEBUG=False` in production
   * Secret key and database credentials stored in environment variables
   * `.env` not committed to version control

[↑ Back to Top](#contents)

---

## Credits

### Code & Frameworks

* **Django** – Web framework
* **Bootstrap** – CSS framework for layout and styling
* **Gunicorn / Whitenoise** – Production server and static files

### Learning Resources

* Code Institute learning materials for Django and back-end development
* Django official documentation
* MDN Web Docs (HTML/CSS/JavaScript references)
* Stack Overflow for targeted debugging

### Acknowledgements

* Code Institute tutors and mentors for guidance on Project 3
* Friends and family who tested the booking flow and gave feedback

---

*This project was built by **Leon Freeman** as part of the Level 5 Diploma in Web Application Development – Unit 3 (Back End Development), demonstrating full-stack capabilities with Django, relational database design, and live deployment.*
