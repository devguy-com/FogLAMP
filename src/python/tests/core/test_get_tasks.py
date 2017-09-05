import asyncio
import datetime
import os
import time
import uuid

import pytest

from foglamp.core.scheduler import (Scheduler, IntervalSchedule, ScheduleNotFoundError, Task,
                                    Schedule, TimedSchedule, ManualSchedule, StartUpSchedule, Where)


__author__ = "Terris Linenbach"
__copyright__ = "Copyright (c) 2017 OSIsoft, LLC"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

class TestScheduler:
    @staticmethod
    async def stop_scheduler(scheduler: Scheduler)->None:
        """stop the schedule process - called at the end of each test"""
        while True:
            try:
                await scheduler.stop()  # Call the stop command
                break
            except TimeoutError:
                await asyncio.sleep(1)

    @pytest.mark.asyncio
    async def test_get_tasks(self):
        """Get list of tasks
        :assert:
            Number of running tasks
            The state of tasks
            the start time of a given task
        """
        scheduler = Scheduler()

        await scheduler.populate_test_data()
        await scheduler.start()

        # declare scheduler task
        interval_schedule = IntervalSchedule()
        interval_schedule.name = 'get_tasks'
        interval_schedule.process_name = "sleep5"
        interval_schedule.repeat = datetime.timedelta(seconds=1)
        interval_schedule.exclusive = False
        await scheduler.save_schedule(interval_schedule)

        await asyncio.sleep(15)

        # Assert running tasks
        tasks = await scheduler.get_tasks(
            where=Task.attr.state == int(Task.State.INTERRUPTED))
        assert not tasks

        tasks = await scheduler.get_tasks(
            where=(Task.attr.end_time == None))
        assert tasks

        tasks = await scheduler.get_tasks(50)
        assert len(tasks) > 1
        assert tasks[0].state == Task.State.RUNNING
        assert tasks[-1].state == Task.State.COMPLETE

        tasks = await scheduler.get_tasks(1)
        assert len(tasks) == 1

        tasks = await scheduler.get_tasks(
            where=Task.attr.state.in_(int(Task.State.RUNNING)),
            sort=[Task.attr.state.desc], offset=50)
        assert not tasks

        tasks = await scheduler.get_tasks(
            where=(Task.attr.state == int(Task.State.RUNNING)).or_(
                Task.attr.state == int(Task.State.RUNNING),
                Task.attr.state == int(Task.State.RUNNING)).and_(
                Task.attr.state.in_(int(Task.State.RUNNING)),
                Task.attr.state.in_(int(Task.State.RUNNING)).or_(
                    Task.attr.state.in_(int(Task.State.RUNNING)))),
            sort=(Task.attr.state.desc, Task.attr.start_time))
        assert tasks

        tasks = await scheduler.get_tasks(
            where=Where.or_(Task.attr.state == int(Task.State.RUNNING),
                            Task.attr.state == int(Task.State.RUNNING)))
        assert tasks

        tasks = await scheduler.get_tasks(
            where=(Task.attr.state == int(Task.State.RUNNING)) | (
                Task.attr.state.in_(int(Task.State.RUNNING))))
        assert tasks

        tasks = await scheduler.get_tasks(
            where=(Task.attr.state == int(Task.State.RUNNING)) & (
                Task.attr.state.in_(int(Task.State.RUNNING))))
        assert tasks

        await self.stop_scheduler(scheduler)
