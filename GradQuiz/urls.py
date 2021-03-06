from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^login/$', 'GradQuiz.views.login'),
	url(r'^invalid_login/$', 'GradQuiz.views.invalid_login'),
	url(r'^user_auth/$', 'GradQuiz.views.user_authentication'),
	url(r'^main_page/$', 'GradQuiz.views.main_page_handler'),
	url(r'^logout/$', 'GradQuiz.views.logout_handler'),
	url(r'^create_user/$', 'GradQuiz.views.createuser_handler'),
	url(r'^course/get/(?P<course_id>\w+)/$', 'GradQuiz.views.course_profs_handler'),
	url(r'^course/(?P<course_id>\w+)/add_homework/$', 'GradQuiz.views.course_add_homework_handler'),
	url(r'^course/(?P<course_id>\w+)/addremove_questions_homework/$', 'GradQuiz.views.course_list_homeworks_handler'),
	url(r'^course/(?P<course_id>\w+)/addremove_questions_homework/(?P<homework_id>\w+)/$', 'GradQuiz.views.addremove_questions_to_homework_handler'),
	url(r'^course/(?P<course_id>\w+)/edit_homeworks/$', 'GradQuiz.views.course_edit_homeworks_display_handler'),
	url(r'^course/(?P<course_id>\w+)/edit_homework/(?P<homework_id>\w+)/$', 'GradQuiz.views.course_edit_homework_handler'),
	url(r'^course/(?P<course_id>\w+)/view_homework/$', 'GradQuiz.views.course_view_homework_handler'),
	url(r'^course/(?P<course_id>\w+)/view_notifications/$', 'GradQuiz.views.course_view_notifications_handler'),
	url(r'^course/(?P<course_id>\w+)/reports/$', 'GradQuiz.views.course_reports_handler'),
	url(r'^course/(?P<course_id>\w+)/homework/(?P<homework_id>\w+)/display_questions/$', 'GradQuiz.views.course_topic_display_questions_handler'),
	url(r'^course/(?P<course_id>\w+)/homework/(?P<homework_id>\w+)/add_questions/$', 'GradQuiz.views.homework_add_questions_handler'),

	#Student URLS
	url(r'^student/select_course/$', 'GradQuiz.views.student_select_course_handler'),
	url(r'^student/course/get/(?P<course_id>\w+)/$', 'GradQuiz.views.student_course_display_details_handler'),
	url(r'^student/add_course/$', 'GradQuiz.views.student_list_all_courses_to_enroll_handler'),
	url(r'^student/course/enroll/(?P<course_id>\w+)/$', 'GradQuiz.views.student_enroll_to_course_handler'),
	url(r'^student/course/enroll/(?P<course_id>\w+)/authorize/$', 'GradQuiz.views.student_authorize_enroll_handler'),
)
