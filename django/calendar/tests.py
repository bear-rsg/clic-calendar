from django.test import TestCase
from django.urls import reverse


class TestQuestionListView(TestCase):
    """
    Test Question List View
    """

    fixtures = ['test.json', ]

    def test_question_list_empty_get(self):
        """
        Empty GET request of the question list page
        should show list of question
        """
        url = reverse('question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Questions</h2>')

    def test_question_list_nonsense_get(self):
        """
        Nonsense GET request of the question list page
        should show list of question
        """
        url = reverse('question-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Questions</h2>')

    def test_question_list_nonsense_post(self):
        """
        Nonsense POST request of the question list page
        should error 405, as POST is not allowed
        """
        url = reverse('question-list')
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestQuestionDetailView(TestCase):
    """
    Test Question Details View
    """

    fixtures = ['test.json', ]

    def test_question_detail_empty_get(self):
        """
        Empty GET request of the question detail page
        should show person's details
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Question ')

    def test_question_detail_nonsense_get(self):
        """
        Nonsense GET request of the question detail page
        should show person's details
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Question ')

    def test_question_detail_nonsense_post(self):
        """
        Nonsense POST request of the question detail page
        should error 405, as POST is not allowed
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestAnswerDetailView(TestCase):
    """
    Test Answer Details View
    """

    fixtures = ['test.json', ]

    def test_answer_detail_empty_get(self):
        """
        Empty GET request of the answer detail page
        should show person's details
        """
        url = reverse('answer-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Answer ')

    def test_answer_detail_nonsense_get(self):
        """
        Nonsense GET request of the answer detail page
        should show person's details
        """
        url = reverse('answer-detail', kwargs={'pk': 1})
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Answer ')

    def test_answer_detail_nonsense_post(self):
        """
        Nonsense POST request of the answer detail page
        should error 405, as POST is not allowed
        """
        url = reverse('answer-detail', kwargs={'pk': 1})
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestAnswerCreateView(TestCase):

    def test_answer_create_empty_get(self):
        """
        Empty GET request of the answer create page
        should show create answer form
        """
        url = reverse('answer-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Share Your Answer</h2>')

    def test_answer_create_nonsense_get(self):
        """
        Nonsense GET request of the answer create page
        should show create answer form
        """
        url = reverse('answer-create')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Share Your Answer</h2>')
