---
aliases: Task Scheduler
tags: 
date created: Saturday, August 19th 2023, 8:26:08 pm
date modified: Saturday, August 19th 2023, 8:30:09 pm
---

![[task-scheduler.svg]]  
Windows Task Scheduler is a component of Microsoft Windows that provides the ability to schedule the launch of programs or scripts at pre-defined times or after specified time intervals. It can be used to automate routine tasks on a computer. Here are some of the main features of Windows Task Scheduler:

1. **Scheduled Tasks**: You can set tasks to run at specific times, on specific days, or after specific intervals.

2. **Event-Based Triggers**: Tasks can be triggered based on specific events. For example, you can set a task to run when the computer starts up, when a user logs on, or when a specific event is logged in the Event Viewer.

3. **Action Types**: When a task is triggered, it can perform various actions such as:
   - Starting a program
   - Sending an email
   - Displaying a message

4. **Conditions**: You can set conditions that must be met for a task to run. For instance, the task might only run if the computer is idle for a certain amount of time, if it's on AC power (not running on battery), or if it's connected to a network.

5. **Settings**: These allow you to control the behavior of the task. For example:
   - Stop the task if it runs longer than a specified time
   - Restart a task if it fails
   - Delete a task if it's not scheduled to run again

6. **Security Options**: You can specify the security context the task runs in. This means you can set which user account the task will run under and whether it requires elevated privileges.

7. **History**: Windows Task Scheduler keeps a history of when tasks are started, run, and completed. This can be useful for troubleshooting.

8. **Integration with Event Viewer**: You can view scheduled task logs in the Event Viewer, which can help in diagnosing issues or ensuring tasks are running as expected.

9. **Multiple Schedules**: A single task can have multiple triggers. For instance, you could set a task to run at both 9 AM every day and also when the computer starts up.

10. **Delay Task for**: You can delay the task from running for a specified time after the trigger is activated.

11. **Repeat Task**: You can set tasks to repeat at regular intervals after they start.

12. **End Task**: You can set conditions to end a running task, such as if it runs for too long.

13. **Network Settings**: You can specify network settings for a task, like running only if a specific network connection is available.

14. **Power Management**: Tasks can be set to wake the computer to run or to not start if the computer is running on batteries.

15. **XML Support**: Task definitions can be exported and imported as XML files, allowing for easy backup, sharing, and replication of tasks.

16. **Compatibility**: Windows Task Scheduler supports backward compatibility, so tasks created in older versions of Windows can still be run in newer versions.
