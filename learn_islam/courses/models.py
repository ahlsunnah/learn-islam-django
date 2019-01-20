from django.db import models
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):

    order = models.PositiveIntegerField(_("Order"), blank=True)
    level = models.PositiveIntegerField(_("Level"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)


# integer not null primary key autoincrement, `track_id` integer not null, `topic_id` integer not null, `order` integer, `slug` varchar(20) not null, `created_at` datetime not null default CURRENT_TIMESTAMP, `updated_at` datetime not null default CURRENT_TIMESTAMP, `level` integer, foreign key(`track_id`) references `tracks`(`id`) on delete CASCADE on update CASCADE, foreign key(`topic_id`) references `topics`(`id`) on delete CASCADE on update CASCADE);

