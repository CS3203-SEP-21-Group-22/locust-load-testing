from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    admin_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IlNtaXRoSkFAdW9lLnVzIiwiY2xpZW50X2lkIjoiZ3JvdXAyMi1jbGllbnQtaWQiLCJpYXQiOjE3MjY3NzgxMzUsImV4cCI6MTcyNjc4MTczNX0.BvNzyFt04TU0PquYVdJ0OqcAQpaDd9_pCRI1sDzBgWU"
    clerk_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkJyb3duVFJAdW9lLnVzIiwiY2xpZW50X2lkIjoiZ3JvdXAyMi1jbGllbnQtaWQiLCJpYXQiOjE3MjY4MjUzNTEsImV4cCI6MTcyNjgyODk1MX0.uniWEUme3zsWh3DaoLpPNJY3uDEdm4BL9ISUW5hE750"
    student_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkhhcnJpc0FHQHVvZS51cyIsImNsaWVudF9pZCI6Imdyb3VwMjItY2xpZW50LWlkIiwiaWF0IjoxNzI3MTE3NTc0LCJleHAiOjE3MjcxMjExNzR9.Z-Rc09X-DqdHVnTsdrNiLzpj82KPvs95CTdDXWXGf24"
    technician_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkxlZUNIQHVvZS51cyIsImZpcnN0TmFtZSI6IkhlbGVuIiwibGFzdE5hbWUiOiJMZWUiLCJjb250YWN0TnVtYmVyIjoiKzQ0NzY1NDMyMTkwIiwiY2xpZW50X2lkIjoiZ3JvdXAyMi1jbGllbnQtaWQiLCJpYXQiOjE3MjUxNjk5NzEsImV4cCI6MTcyNTE3MDg3MX0.hnX0vyqhrVXGHOvLxQTJRDjynOyxw7wkgBOpFXmwmEA"

    def on_start(self):
        """ This method runs when a user starts, and you can use it to set up the bearer token. """
        self.admin_headers = {
            "Authorization": f"Bearer {self.admin_token}"
        }
        self.clerk_headers = {
            "Authorization": f"Bearer {self.clerk_token}"
        }
        self.student_headers = {
            "Authorization": f"Bearer {self.student_token}"
        }
        self.technician_headers = {
            "Authorization": f"Bearer {self.technician_token}"
        }

    @task
    def test_index(self):
        self.client.get("/")

    @task
    def test_query_equipment_reservations(self):
        self.client.get("/api/admin/reservations/1", headers=self.admin_headers)

    @task
    def test_query_maintenance(self):
        self.client.get("/api/clerk/maintenance", headers=self.clerk_headers)
    
    @task
    def test_query_reservations(self):
        self.client.get("/api/student/reservations", headers=self.student_headers)

    @task
    def test_query_assigned_maintenance(self):
        self.client.get("/api/technician/maintenance", headers=self.technician_headers)

    @task
    def test_query_equipments(self):
        self.client.get("/api/user/equipments?labId=1", headers=self.student_headers)

    @task
    def test_query_labs(self):
        self.client.get("/api/user/labs", headers=self.admin_token)
    
    @task
    def test_query_user_roles(self):
        self.client.get("/api/user/role", headers=self.technician_headers)
