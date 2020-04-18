import os
import re
import sys
from send_email_config import *
import smtplib


def doYouWantDeploy():
    user_input = raw_input('Do you want to deploy this push? (Y or y to proceed)')
    return user_input.upper() == 'Y'


def getEmailBodyFromCommitMessage():
    user_input = raw_input('How many commit messages do you want to add in the Email? (Default with 1)')
    if user_input == '':
        user_input = DEFAULT_COMMIT_MSG_NUMBER
    commit_msg = os.popen("git log -{} --pretty=%B".format(user_input)).read().strip()
    return '\n\n'.join([msg for msg in commit_msg.strip('\n') if re.search('test', msg, re.IGNORECASE)])


def getEmailBodyFromUserInput():
    user_input = raw_input('What message do you want to add in this email?')
    return user_input


def getEmailBody():
    user_input = raw_input('Do you want use your commit message as email body? (Default with Y)')
    if user_input == '' or user_input.upper() == 'Y':
        return getEmailBodyFromCommitMessage()
    return getEmailBodyFromUserInput()


def getCurrentBranch():
    commit_msg_commander = 'git rev-parse --abbrev-ref HEAD'
    return os.popen(commit_msg_commander).read().strip()


def chooseSubjectAndNotifyList(current_branch):
    user_input = raw_input('Which environment do you want deploy? (Default with SYS)')
    if user_input == '' or user_input.upper() not in ENVIRONMENT_LIST or user_input.upper() == ENVIRONMENT_LIST[0]:
        return [SUBJECT.format(current_branch, ENVIRONMENT_LIST[0], WAITING_TIME_LIST[0]), EMAIL_NOTIFY_LIST_SYS]
    return [SUBJECT.format(current_branch, ENVIRONMENT_LIST[1], WAITING_TIME_LIST[1]), EMAIL_NOTIFY_LIST_UAT]


sys.stdin = open('CON', 'r')
need_send_email = doYouWantDeploy()

if need_send_email is True:
    commit_msg = getEmailBody()
    current_branch = getCurrentBranch()
    subjectAndNotifyList = chooseSubjectAndNotifyList(current_branch)
    email_message = EMAIL_MESSAGE_TEMPLATE.format(EMAIL_ACCOUNT, ', '.join(subjectAndNotifyList[1]),
                                                  subjectAndNotifyList[0], commit_msg, USER_NAME)
    server = smtplib.SMTP(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT)
    server.sendmail(EMAIL_ACCOUNT, subjectAndNotifyList[1], email_message)
    server.quit()
