_base_ = ['./ssd300_voc0712.py']
data_root = 'data/VOCdevkit/'
model = dict(
    bbox_head=dict(
        num_classes=1
    )
)
data = dict(
    train=dict(
        times=3,
        dataset=dict(
            ann_file=[data_root + 'VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'VOC2007/'],
        ),
    ),
    val=dict(
        ann_file=data_root + 'VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root + 'VOC2007/',
    ),
    test=dict(
        ann_file=data_root + 'VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root + 'VOC2007/',
    )
)
