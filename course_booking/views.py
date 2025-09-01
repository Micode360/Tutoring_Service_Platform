from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseBookingSerializer
from .models import CourseBooking

# Create your views here.
class ApplyView(APIView):
    def put(self, request):
        session_booking_data = request.data.copy()
        print(session_booking_data)

        try:
            find_session_via_tutor = CourseBooking.objects.filter(tutor=session_booking_data["tutor"]).first()
        except CourseBooking.DoesNotExist:
             return Response({"message": "This tutor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if find_session_via_tutor:
            find_session_via_tutor.students

            initial_session = {"tutor": session_booking_data["tutor"], "students": [session_booking_data["student"]]}
            serializer = CourseBookingSerializer(data=initial_session)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "You have successfully joined the course."}, status=status.HTTP_201_CREATED)  
        else:
            initial_session = {"tutor": session_booking_data["tutor"], "students": [session_booking_data["student"]]}
            serializer = CourseBookingSerializer(data=initial_session)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "You have successfully booked a course."}, status=status.HTTP_201_CREATED)
        
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
