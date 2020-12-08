from django.test import TestCase
from django.urls import reverse


class TestQuestionListView(TestCase):
    """
    Test Question List View
    """

    fixtures = ['testdata.json', ]

    def test_question_list_empty_get(self):
        """
        Empty GET request of the question list page
        should show list of published questions but not unpublished questions
        """
        url = reverse('question-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Calendar</h2>')
        self.assertContains(response, 'published question')
        self.assertNotContains(response, 'unpublished question')

    def test_question_list_nonsense_get(self):
        """
        Nonsense GET request of the question list page
        should show list of published questions but not unpublished questions
        """
        url = reverse('question-list')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Calendar</h2>')
        self.assertContains(response, 'published question')
        self.assertNotContains(response, 'unpublished question')

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

    fixtures = ['testdata.json', ]

    def test_question_detail_empty_get(self):
        """
        Empty GET request of the question detail page should show:
        - question details
        - 'share your answer' section
        - list of approved answers (and ignore unapproved answers)
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'published question')
        self.assertContains(response, '<h2>Share Your Answer</h2>')
        self.assertContains(response, '<h2>All Answers</h2>')
        self.assertContains(response, 'approved answer')
        self.assertNotContains(response, 'unapproved answer')

    def test_question_detail_nonsense_get(self):
        """
        Empty GET request of the question detail page should show:
        - question details
        - 'share your answer' section
        - list of approved answers (and ignore unapproved answers)
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'published question')
        self.assertContains(response, '<h2>Share Your Answer</h2>')
        self.assertContains(response, '<h2>All Answers</h2>')
        self.assertContains(response, 'approved answer')
        self.assertNotContains(response, 'unapproved answer')

    def test_question_detail_unpublished_question(self):
        """
        GET request of the question detail page
        for an unpublished question should show 404
        """
        url = reverse('question-detail', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_question_detail_nonsense_post(self):
        """
        Nonsense POST request of the question detail page
        should error 405, as POST is not allowed
        """
        url = reverse('question-detail', kwargs={'pk': 1})
        response = self.client.post(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 405)


class TestAnswerCreateSuccessView(TestCase):

    def test_answer_create_empty_get(self):
        """
        Empty GET request of the answer create page
        should show create answer form
        """
        url = reverse('answer-create-success')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your answer has been sent to us successfully.')

    def test_answer_create_nonsense_get(self):
        """
        Nonsense GET request of the answer create page
        should show create answer form
        """
        url = reverse('answer-create-success')
        response = self.client.get(url, {'nonsense': 'aaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your answer has been sent to us successfully.')
