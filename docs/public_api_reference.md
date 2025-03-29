# Public API Reference

## Types of resources

### Package

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```
### PackageInfo

`PackageInfo` is a `Package`, but without `data` property

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

## Urls

All urls are relative `<domain>://api_v1`

### Get Package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

### Get Package Info

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package_info`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

> [!NOTE]
> `PackageInfo` does not contain `data` property
