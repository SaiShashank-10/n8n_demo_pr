# 🤖 AI-Powered PR Review Workflow (n8n)

[![n8n](https://img.shields.io/badge/Built%20with-n8n-ef6c00?logo=n8n&logoColor=white)](https://n8n.io/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI-412991?logo=openai&logoColor=white)](https://openai.com/)
[![GitHub](https://img.shields.io/badge/Integrates-GitHub-181717?logo=github&logoColor=white)](https://github.com/)
[![Repo Stars](https://img.shields.io/github/stars/SaiShashank-10/n8n_demo_pr?style=social)](https://github.com/SaiShashank-10/n8n_demo_pr)
[![Last Commit](https://img.shields.io/github/last-commit/SaiShashank-10/n8n_demo_pr)](https://github.com/SaiShashank-10/n8n_demo_pr/commits)

An automated **Pull Request Review pipeline** built with **n8n + OpenAI + GitHub**.
It listens for PR events, collects diffs, generates a focused review prompt, runs an AI code review agent, posts the review, and labels the PR.

---

## 📸 Workflow Preview

![n8n workflow](https://github.com/user-attachments/assets/0b2aa1e9-11c1-4a7a-aa05-e5934cb5a56d)

---

## ⚙️ Workflow Steps

1. **PR Review (Trigger)**  
   Starts the flow when a pull request event is received.
2. **Get file's Diffs from PR**  
   Fetches changed files and patch/diff details from GitHub.
3. **Create target Prompt from PR Diffs**  
   Builds a review-focused prompt from changed code.
4. **Code Review Agent (OpenAI Chat Model)**  
   Generates structured AI review feedback.
5. **GitHub Robot (create: review)**  
   Posts review comments/results back to the pull request.
6. **Add Label to PR**  
   Applies a label to indicate review status.

---

## ✨ Highlights

- Automated AI-assisted PR reviews
- Diff-aware prompt generation
- GitHub-native review publishing
- Label-based review state tracking
- Fully visual, extensible n8n workflow

---

## 🧩 Tech Stack

- **n8n** (workflow orchestration)
- **OpenAI Chat Model** (review intelligence)
- **GitHub API / Nodes** (PR integration)

---

## 🚀 Getting Started

1. Open your n8n instance.
2. Recreate/import this workflow.
3. Configure credentials:
   - GitHub credentials
   - OpenAI API credentials
4. Set repository + PR event trigger.
5. Activate the workflow.

---

## 📌 Notes

- Tune prompt quality in the **Create target Prompt from PR Diffs** node.
- Add extra decision nodes for stricter review rules (security, style, tests, etc.).
- Extend with Slack/Email notifications if needed.
