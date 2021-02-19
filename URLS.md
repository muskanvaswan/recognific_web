**/** base.views.index	index <br>
**/about/**	base.views.about	about<br>
**/accounts/login/**	base.views.sign_in	login<br>
**/accounts/logout/**	base.views.log_out_view	logout<br>
**/accounts/sign_up/**	base.views.sign_up	sign_up<br>
**/accounts/sign_up_as/**	base.views.sign_up_as  sign_up_as<br>
**/accounts/user/<pk>**	base.views.UserUpdateView	user_update<br>
**/admin/**	django.contrib.admin.sites.index	admin:index<br>
**/admin/<app_label>/**	django.contrib.admin.sites.app_index	admin:app_list<br>
**/admin/auth/user/**	django.contrib.admin.options.changelist_view	admin:auth_user_changelist<br>
**/admin/auth/user/<id>/password/**	django.contrib.auth.admin.user_change_password	admin:auth_user_password_change<br>
**/admin/auth/user/<path:object_id>/**	django.views.generic.base.RedirectView<br>
**/admin/auth/user/<path:object_id>/change/**	django.contrib.admin.options.change_view	admin:auth_user_change<br>
**/admin/auth/user/<path:object_id>/delete/**	django.contrib.admin.options.delete_view	admin:auth_user_delete<br>
**/admin/auth/user/<path:object_id>/history/**	django.contrib.admin.options.history_view	admin:auth_user_history<br>
**/admin/auth/user/add/**	django.contrib.auth.admin.add_view	admin:auth_user_add<br>
**/admin/auth/user/autocomplete/**	django.contrib.admin.options.autocomplete_view	admin:auth_user_autocomplete<br>
**/admin/base/teacher/**	django.contrib.admin.options.changelist_view	admin:base_teacher_changelist<br>
**/admin/base/teacher/<path:object_id>/**	django.views.generic.base.RedirectView<br>
**/admin/base/teacher/<path:object_id>/change/**	django.contrib.admin.options.change_view	admin:base_teacher_change<br>
**/admin/base/teacher/<path:object_id>/delete/**	django.contrib.admin.options.delete_view	admin:base_teacher_delete<br>
**/admin/base/teacher/<path:object_id>/history/**	django.contrib.admin.options.history_view	**admin:base_teacher_history<br>
**/admin/base/teacher/add/**	django.contrib.admin.options.add_view	admin:base_teacher_add<br>
**/admin/base/teacher/autocomplete/**	django.contrib.admin.options.autocomplete_view	admin:base_teacher_autocomplete<br>
**/admin/encode/classset/**	django.contrib.admin.options.changelist_view	admin:encode_classset_changelist<br>
**/admin/encode/classset/<path:object_id>/**	django.views.generic.base.RedirectView<br>
**/admin/encode/classset/<path:object_id>/change/**	django.contrib.admin.options.change_view	admin:encode_classset_change<br>
**/admin/encode/classset/<path:object_id>/delete/**	django.contrib.admin.options.delete_view	admin:encode_classset_delete<br>
**/admin/encode/classset/<path:object_id>/history/**	django.contrib.admin.options.history_view	admin:encode_classset_history<br>
**/admin/encode/classset/add/**	django.contrib.admin.options.add_view	admin:encode_classset_add<br>
**/admin/encode/classset/autocomplete/**	django.contrib.admin.options.autocomplete_view	admin:encode_classset_autocomplete<br>
**/admin/encode/student/**	django.contrib.admin.options.changelist_view	admin:encode_student_changelist<br>
**/admin/encode/student/<path:object_id>/**	django.views.generic.base.RedirectView
**/admin/encode/student/<path:object_id>/change/**	django.contrib.admin.options.change_view	admin:encode_student_change<br>
**/admin/encode/student/<path:object_id>/delete/**	django.contrib.admin.options.delete_view	admin:encode_student_delete<br>
**/admin/encode/student/<path:object_id>/history/**	django.contrib.admin.options.history_view	admin:encode_student_history<br>
**/admin/encode/student/add/**	django.contrib.admin.options.add_view	admin:encode_student_add<br>
**/admin/encode/student/autocomplete/**	django.contrib.admin.options.autocomplete_view	admin:encode_student_autocomplete<br>
**/admin/jsi18n/**	django.contrib.admin.sites.i18n_javascript	admin:jsi18n<br>
**/admin/login/**	django.contrib.admin.sites.login	admin:login<br>
**/admin/logout/**	django.contrib.admin.sites.logout	admin:logout<br>
**/admin/password_change/**	django.contrib.admin.sites.password_change	admin:password_change<br>
**/admin/password_change/done/**	django.contrib.admin.sites.password_change_doneadmin:password_change_done<br>
**/admin/r/<int:content_type_id>/<path:object_id>/**	django.contrib.contenttypes.views.shortcut	admin:view_on_site<br>
**/admin/recognize/attendance/**	django.contrib.admin.options.changelist_view	admin:recognize_attendance_changelist
**/admin/recognize/attendance/<path:object_id>/	django.views.generic.base.RedirectView<br>
**/admin/recognize/attendance/<path:object_id>/change/**	django.contrib.admin.options.change_view	admin:recognize_attendance_change<br>
**/admin/recognize/attendance/<path:object_id>/delete/**	django.contrib.admin.options.delete_view	admin:recognize_attendance_delete<br>
**/admin/recognize/attendance/<path:object_id>/history/**	django.contrib.admin.options.history_view	admin:recognize_attendance_history<br>
**/admin/recognize/attendance/add/**	django.contrib.admin.options.add_view	admin:recognize_attendance_add<br>
**/admin/recognize/attendance/autocomplete/**	django.contrib.admin.options.autocomplete_view	admin:recognize_attendance_autocomplete<br>
**/contact/**	base.views.ContactView	contact<br>
**/dashboard/**	encode.views.DashboardView	dashboard<br>
**/dashboard/class/<int:classset_id>/**	encode.views.ClassSetDetailView	class_details<br>
**/dashboard/class/activate/<int:classset_id>/**	encode.views.activate_class_setactivate<br>
**/dashboard/class/deactivate/<int:classset_id>/**	encode.views.deactivate_class_set	deactivate<br>
**/dashboard/classset/create/**	encode.views.ClassSetCreateView	create_classset<br>
**/dashboard/classset/update/<pk>/**	encode.views.ClassSetUpdateView	update_classset<br>
**/dashboard/profile**	encode.views.Profile	profile<br>
**/dashboard/student/create/**	encode.views.StudentCreateView	create_student
/media/<path>	django.views.static.serve<br>
**/r/api/make_sheet/<int:classname>/**	recognize.views.attendace_api	make_attendance<br>
**/r/cam/<str:classname>/**	recognize.views.stream_view	camera<br>
**/r/face/<str:classname>/**	recognize.views.face_view	face<br>
