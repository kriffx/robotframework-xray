import json, requests
from ntpath import join
from .config import Config
from datetime import datetime

class Xray:
    
    
    def authentication() -> str:
        XRAY_API = Config.xray_api()
        XRAY_CLIENT_ID = Config.xray_client_id()
        XRAY_CLIENT_SECRET = Config.xray_client_secret()

        json_data = json.dumps({'client_id': XRAY_CLIENT_ID, 'client_secret': XRAY_CLIENT_SECRET})
        resp = requests.post(f'{XRAY_API}/authenticate', data=json_data, headers={'Content-Type':'application/json'})
            
        if resp.status_code == 200:
            return f'Bearer {resp.json()}'
        else:
            print('Authentication error: ', resp.status_code)


    # def updateXrayTest(issueId: str, unstructured: str):
    #     XRAY_API = Config.xray_api()

    #     auth_token = Xray.authentication()
    #     unstructured = unstructured.encode('unicode_escape').decode()
    #     unstructured = unstructured.replace('    ', '\\t')
    #     unstructured = unstructured.replace('"', '\\"')
        
    #     json_data = f'''
    #         mutation {{
    #             updateUnstructuredTestDefinition(issueId: "{ issueId }", unstructured: "{ unstructured }") {{
    #                 issueId
    #                 unstructured
    #             }}
    #         }}
    #     '''

    #     resp = requests.post(
    #         f'{XRAY_API}/graphql',
    #         json={
    #             'query': json_data
    #         },
    #         headers={
    #             'Content-Type': 'application/json',
    #             'Authorization': auth_token
    #         },
    #     )

    #     if resp.status_code == 200:
    #         return resp.json()
    #     else:
    #         print('Error updating xray test, trying again...')


    # def updateXrayTestType(issueId: str):
    #     XRAY_API = Config.xray_api()
    #     auth_token = Xray.authentication()
        
    #     json_data = f'''
    #         mutation {{
    #             updateTestType(issueId: "{ issueId }", testType: {{ name: "Generic" }} ) {{
    #                 issueId
    #                 testType {{
    #                     name
    #                     kind
    #                 }}
    #             }}
    #         }}
    #     '''

    #     resp = requests.post(
    #         f'{XRAY_API}/graphql',
    #         json={
    #             'query': json_data
    #         },
    #         headers={
    #             'Content-Type': 'application/json',
    #             'Authorization': auth_token
    #         },
    #     )

    #     if resp.status_code != 200:
    #         print('Error updating xray test type, trying again...')
    
    def addVideoEvidenceToTestRun(id: int, filename: str, data: str):
        XRAY_API = Config.xray_api()

        json_data = f'''
            mutation {{
                addEvidenceToTestRun(
                    id: "{ id }",
                    evidence: [
                        {{
                            filename: "{ filename }"
                            mimeType: "video/mp4"
                            data: "{ data }"
                        }}
                    ]
                ) {{
                    addedEvidence
                    warnings
                }}
            }}
        '''

        resp = requests.post(
            f'{XRAY_API}/graphql',
            json={
                'query': json_data
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': Xray.authentication()
            },
        )

        if resp.status_code != 200:
            print('Error sending video evidence: ', resp.status_code)
        else:
            print('Video evidence successfully saved.')


    def getTest(testKey: str):
        XRAY_API = Config.xray_api()

        json_data = f'''
            {{
                getTests(
                    jql: "key = '{ testKey }'",
                    limit: 1
                ) {{
                    results {{
                        issueId
                    }}
                }}
            }}
        '''

        resp = requests.get(
            f'{XRAY_API}/graphql',
            json={'query': json_data},
            headers={
                'Content-Type': 'application/json',
                'Authorization': Xray.authentication()
            },
        )

        if resp.status_code == 200:
            issueId = resp.json().get('data').get('getTests').get('results')[0].get('issueId')
            print('Issue ID = ', issueId)
            return issueId
        else:
            print('Error getting test ID: ', resp.status_code)
    

    def getTestRun(testIssueId: str, testExecutionIssueId: str):
        XRAY_API = Config.xray_api()

        json_data = f'''
            {{
                getTestRun(
                    testIssueId: "{ testIssueId }",
                    testExecIssueId: "{ testExecutionIssueId }"
                ) {{id }}
            }}
        '''

        resp = requests.get(
            f'{XRAY_API}/graphql',
            json={'query': json_data},
            headers={
                'Content-Type': 'application/json',
                'Authorization': Xray.authentication()
            },
        )

        if resp.status_code == 200:
            testRunId = resp.json().get('data').get('getTestRun').get('id')
            print('Test run ID = ', testRunId)
            return testRunId
        else:
            print('Error getting run ID: ', resp.status_code)
    

    def createTestExecution():
        PROJECT_KEY = Config.project_key()
        XRAY_API = Config.xray_api()
        test_execution_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        json_data = f'''
            mutation {{
                createTestExecution(
                    testIssueIds: [],
                    testEnvironments: [],
                    jira: {{
                        fields: {{
                            summary: "QA Automation Execution | { test_execution_date }",
                            project: {{ key: "{ PROJECT_KEY }" }}
                        }}
                    }}
                ) {{
                    testExecution {{
                        issueId
                        jira(fields: ["key"])
                    }}
                    warnings
                    createdTestEnvironments
                }}
            }}
        '''

        resp = requests.post(
            f'{XRAY_API}/graphql',
            json={ 'query': json_data },
            headers={
                'Content-Type': 'application/json',
                'Authorization': Xray.authentication()
            },
        )

        result = json.dumps({
            'issueId': resp.json().get('data').get('createTestExecution').get('testExecution').get('issueId'),
            'key': resp.json().get('data').get('createTestExecution').get('testExecution').get('jira').get('key')
        })

        if resp.status_code == 200:
            print('Created new test execution.')
            return json.loads(result)
        else:
            print('Error create test execution: ', resp.json())
    

    def importExecutionRobot():
        PROJECT_KEY = Config.project_key()
        XRAY_API = Config.xray_api()
        testExecKey = Xray.createTestExecution()

        report = requests.post(f'{XRAY_API}/import/execution/robot', 
            data=open('report.xml', 'rb'),
            params={
                'projectKey': PROJECT_KEY,
                'testExecKey': testExecKey['key'],
            },
            headers={
                'Content-Type': 'application/xml',
                'Authorization': Xray.authentication()
            }
        )

        resp = json.dumps({
            'issueId': testExecKey['issueId'],
            'key': report.json().get('key')
        })

        if report.status_code == 200:
            return json.loads(resp)
        else:
            print('Error import execution')


    def importExecutionCucumber():
        PROJECT_KEY = Config.project_key()
        XRAY_API = Config.xray_api()
        # testExecKey = Xray.createTestExecution()

        print("cucumber.json file path:", join(Config.cucumber_path(), 'cucumber.json'))

        report = requests.post(f'{XRAY_API}/import/execution/cucumber', 
            data = open(join(Config.cucumber_path(), 'cucumber.json'), 'rb'),
            params = { 
                'projectKey': PROJECT_KEY,
                # 'testExecKey': testExecKey['key'],
            },
            headers = {
                'Content-Type': 'application/json',
                'Authorization': Xray.authentication()
            }
        )

        if report.status_code != 200:
            print('Error Cucumber import execution.')
            print('Retorno: ', report.json())
        else:
            print('Successfully sent Cucumber import execution.')
            print('Retorno: ', report.status_code)
