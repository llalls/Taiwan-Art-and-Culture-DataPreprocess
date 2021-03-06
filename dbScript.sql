USE [Activity]
GO
/****** Object:  Table [dbo].[activityInfo]    Script Date: 2021/12/26 下午 08:52:24 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[activityInfo](
	[version] [float] NULL,
	[UID] [nvarchar](255) NULL,
	[title] [nvarchar](255) NULL,
	[category] [int] NULL,
	[showUnit] [nvarchar](255) NULL,
	[descriptionFilterHtml] [nvarchar](max) NULL,
	[discountInfo] [nvarchar](max) NULL,
	[imageUrl] [nvarchar](max) NULL,
	[masterUnit] [nvarchar](255) NULL,
	[subUnit] [nvarchar](255) NULL,
	[supportUnit] [nvarchar](255) NULL,
	[otherUnit] [nvarchar](255) NULL,
	[webSales] [nvarchar](max) NULL,
	[sourceWebPromote] [nvarchar](max) NULL,
	[comment] [nvarchar](max) NULL,
	[editModifyDate] [nvarchar](255) NULL,
	[sourceWebName] [nvarchar](max) NULL,
	[startDate] [datetime] NULL,
	[endDate] [datetime] NULL,
	[hitRate] [int] NULL,
	[showInfo] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[city]    Script Date: 2021/12/26 下午 08:52:24 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[city](
	[city] [nvarchar](32) NULL,
	[cityIndex] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[showInfo]    Script Date: 2021/12/26 下午 08:52:24 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[showInfo](
	[UID] [nvarchar](255) NULL,
	[time] [datetime] NULL,
	[location] [nvarchar](255) NULL,
	[locationName] [nvarchar](255) NULL,
	[onSales] [int] NULL,
	[price] [nvarchar](max) NULL,
	[latitude] [float] NULL,
	[longitude] [float] NULL,
	[endTime] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
