**The problem:**

Trail organizations keep their trails safe and open with small staff and a lot of volunteers. Most of them coordinate everything through spreadsheets, emails, group texts, and paper sign-up sheets. There are many problems with this system:

1. Maintenance issues get reported in different places, so some get lost or fixed late.  
2. Admins can’t easily see which trails need work the most.  
3. Volunteers don’t know what projects are available or when.  
4. Equipment gets double-booked or goes missing because nobody tracks who has it.

**Our solution:**

TrailTrack puts trails, issues, volunteers, and equipment on one website, so the organization responsible for whatever trail can see everything in one place and fix problems faster.

Things to decide and do:

1. We should add a real statistic about trail maintenance.

**Who uses it:**

| Role | Login required | What they can do |
| :---- | :---- | :---- |
| Public visitor | No | View trails and their status, view the issue map, report an issue, create an account if they want to become a volunteer or admin |
| Volunteer | Yes | Everything a visitor can do, plus sign up for projects and see their upcoming projects |
| Admin | Yes | Everything, plus manage trails, update and assign issues, create projects, manage equipment, and view analytics |
| TrailTrack team | Yes | Approve the first admin for each new organization |

Login rules:

1. Volunteers create their own accounts.  
2. Admin accounts have to be approved by the TrailTrack team.  
3. If an organization has multiple admins, the first admin approved by the TrailTrack team can approve additional admins. Which means, the TrailTrack Team shouldn’t be receiving any more notifications to approve admins for an organization with an already approved admin.  
4. Reporting an issue doesn’t need a login, so a hiker on the trail can report a fallen tree in seconds.

**Features:**

| Feature | What it does | Who uses it |
| :---- | :---- | :---- |
| Accounts and approval | Volunteers sign up, admins get approved, organizations stay separate | Everyone with a login |
| Trail dashboard | Shows each trail’s length, difficulty, condition, open/closed status, and active issues | Everyone |
| Issue reporting | Report a problem with a location, type, description, photo, and priority | Everyone |
| Issue tracking | Admins assign issues and update their status | Admins |
| Volunteer projects | Admins create work projects, volunteers sign up until spots are full | Admins, volunteers |
| Equipment tracking | Tracks every tool and blocks reserving something that’s already taken | Admins |
| Issue map | Shows issues as markers colored and labeled by priority | Everyone |
| Analytics | Shows totals and charts like issues by type and volunteer hours | Admins |

**Status flows:**

| Item | Statuses |
| :---- | :---- |
| Issue | Reported \-\> Assigned \-\> In progress \-\> Completed |
| Equipment | Available \-\> Reserved \-\> In use \-\> Maintenance |
| Admin account | Pending \-\> Approved |
