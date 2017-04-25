from behave import given, when, then
import re
from login_utils import *
import time
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


@when(u'a user visits the login page')
def visit_login(context):
    context.browser.get(context.server_address + "/login")


@then(u'she should see the username field')
def see_username_field(context):
    username_found = re.search("username", context.browser.page_source, re.IGNORECASE)
    assert username_found

@then(u'she should see the password field')
def see_password_field(context):
    password_found = re.search("password", context.browser.page_source, re.IGNORECASE)
    assert password_found


@then(u'she should see the login button')
def see_login_button(context):
    login_found = re.search("login", context.browser.page_source, re.IGNORECASE)
    assert login_found

@when(u'she logs in with username "{username}" and password "{password}"')
def login(context, username, password):
    uname = context.browser.find_element_by_name('username')
    passwd = context.browser.find_element_by_name('password')
    login_button = context.browser.find_element_by_id('btn_login')
    uname.clear()
    passwd.clear()
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()


@then(u'she should see a message of login success')
def see_login_success(context):
    success_found = re.search("Login Success!", context.browser.page_source, re.IGNORECASE)
    assert success_found



@then(u'she should see a message of login failure')
def see_login_failure(context):
    fail_found = re.search("Bad Login", context.browser.page_source, re.IGNORECASE)
    assert fail_found


@given(u'a user visits the login page')
def visits_login(context):
    context.browser.get(context.server_address + "/login")


@given(u'she sees the Logout link')
def see_logout_button(context):
    logout_found = re.search("log out", context.browser.page_source, re.IGNORECASE)
    assert logout_found
    time.sleep(0.5)


@when(u'she clicks on the Logout link')
def click_logout_link(context):
    logout_button=context.browser.find_element_by_link_text('log out')
    logout_button.click()
    time.sleep(2)


@then(u'she returns to the site')
def visit_site(context):
    pass
    time.sleep(0.5)

@then(u'she sees a message telling her she has logged out')
def see_logout_success(context):
    logout_success_found = re.search("You were logged out", context.browser.page_source, re.IGNORECASE)
    time.sleep(0.5)
    assert logout_success_found
